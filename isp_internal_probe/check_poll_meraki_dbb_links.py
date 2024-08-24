import mysql.connector
from config_class import config
import datetime
import multiprocessing
from multiprocessing import Manager
import time
from paramiko.ssh_exception import AuthenticationException
from config_class import config
import requests



def find_plj_for_meraki_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, device_serial, default_gateway, api_key, api_port):
    url = f"""https://api.meraki.com/api/v1/devices/{device_serial}/lossAndLatencyHistory"""
    payload = f"""ip=8.8.8.8&resolution=60&uplink={if_name}&timespan=300"""
    headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    # print(url, payload, headers)
    response = requests.get(url, headers=headers, data=payload)
    data_arr = response.json()
    # print(data_arr)

    min_rtt = 0
    avg_rtt = 0
    max_rtt = 0
    jitter = 0
    packet_loss = 100

    if response.status_code == 429:
        time.sleep(1)
        response = requests.get(url, headers=headers, data=payload)
        data_arr = response.json()

    if len(data_arr) > 2:
        last_data = data_arr[-2]
        min_rtt = 0 if last_data['latencyMs'] is None else last_data['latencyMs']
        avg_rtt =  0 if last_data['latencyMs'] is None else last_data['latencyMs']
        max_rtt =  0 if last_data['latencyMs'] is None else last_data['latencyMs']
        jitter = 0 if last_data['jitter'] is None else last_data['jitter']
        packet_loss = last_data['lossPercent']
        
        if last_data['lossPercent'] is None or last_data['lossPercent'] == 'NULL':
            time.sleep(2)
            response = requests.get(url, headers=headers, data=payload)
            data_arr = response.json()
            if len(data_arr) > 2:
                last_data = data_arr[-2]
                min_rtt = 0 if last_data['latencyMs'] is None else last_data['latencyMs']
                avg_rtt =  0 if last_data['latencyMs'] is None else last_data['latencyMs']
                max_rtt =  0 if last_data['latencyMs'] is None else last_data['latencyMs']
                jitter = 0 if last_data['jitter'] is None else last_data['jitter']
                packet_loss = 0 if last_data['lossPercent'] is None else last_data['lossPercent']
                print("Entered here", isp_wan_id, last_data)

    status = 1

    if packet_loss == 100:
        status = 0
        min_rtt = 0
        max_rtt = 0
        avg_rtt = 0
        jitter = 0

    isp_data = {
                "isp_wan_id": isp_wan_id,
                "client_id": cust_id,
                "circuit_id": "NA",
                "public_ip": internal_ip,
                "min_rtt": min_rtt,
                "avg_rtt": avg_rtt,
                "max_rtt": max_rtt,
                "jitter": jitter,
                "packet_loss": packet_loss,
                "status": status,
                    
                "dg_ip": default_gateway,
                "dg_status": 1,
                "dg_min_rtt": 0,
                "dg_max_rtt": 0,
                "dg_avg_rtt": 0,
                "dg_jitter": 0,
                "dg_packet_loss": 0,
                "time": start_time
            }
    
    print(isp_data)

    # Push Data to core
    creds = config.creds
    server = config.server
    cust_id = config.client_id
    
    json_data = {
        "creds": creds,
        "isp_data": isp_data
    }
    try:
        api_path = server + "api/push_isp_data.php"
        api_response = requests.post(api_path, json=json_data, verify=False)
        print(api_response.json())
    except Exception as e:
        print("Error in Pushing Data", e)

    pass


def get_plj_dbb_link(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port, vendor, type, device_serial, default_gateway, api_key, api_port):

    if vendor == 'Meraki':
        find_plj_for_meraki_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, device_serial, default_gateway, api_key, api_port)
    return


if __name__ == "__main__":
    conn = mysql.connector.connect(
        host=config.mysql_conf["host"],
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        port=config.mysql_conf["port"],
        database=config.mysql_conf["database"],
        auth_plugin=config.mysql_conf["auth_plugin"]
    )
    cursor = conn.cursor()

    now = datetime.datetime.now()
    start_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: DBB links polling started Started at:{start_time}")
    
    successful_ips = Manager().list()
    failed_ips = Manager().list()

    process_list = []

    dbb_links_sql = f"""SELECT fn_isp_details.cust_id, 
                            fn_isp_details.isp_wan_id, 
                            fn_isp_details.internal_ip, 
                            fn_isp_details.if_name, 
                            fn_isp_details.if_index, 
                            fn_edge_devices.device_id,
                            fn_edge_devices.device_ip,
                            fn_edge_devices.ssh_username,
                            fn_edge_devices.ssh_password,
                            fn_edge_devices.ssh_port,
                            fn_edge_devices.vendor,
                            fn_edge_devices.`type`,
                            fn_edge_devices.device_serial,
                            fn_isp_details.default_gateway,
                            fn_edge_devices.api_key,
                            fn_edge_devices.api_port		
                FROM fn_isp_details, fn_edge_devices
                WHERE fn_isp_details.link_type='DBB' AND fn_isp_details.edge_device_id=fn_edge_devices.device_id AND fn_edge_devices.vendor='Meraki' AND fn_edge_devices.device_id=1165"""
    
    cursor.execute(dbb_links_sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    # Create processes for each device
    index = 0
    for row in result:
        cust_id = row[0]
        isp_wan_id = row[1]
        internal_ip = row[2]
        if_name = row[3]
        if_index = row[4]
        device_id = row[5]
        device_ip = row[6]
        ssh_username = row[7]
        ssh_password = row[8]
        ssh_port = row[9]
        vendor = row[10]
        type = row[11]
        device_serial = row[12]
        default_gateway = row[13]
        api_key = row[14]
        api_port = row[15]
        
        process = multiprocessing.Process(target=get_plj_dbb_link, args=(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port, vendor, type, device_serial, default_gateway, api_key, api_port))
        process_list.append(process)

        if index % 10 == 0 or index == (cursor.rowcount-1):
            for process in process_list:
                process.start()

            for process in process_list:
                process.join()

            process_list = []
            time.sleep(2)

        index = index + 1

    # Print the summary
    now = datetime.datetime.now()
    end_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: DBB links polling Completed at:{end_time}")
