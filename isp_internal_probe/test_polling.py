import mysql.connector
import subprocess
from config_class import config
import datetime
import multiprocessing
from multiprocessing import Manager
import subprocess
import paramiko
import time
import re
from paramiko.ssh_exception import AuthenticationException
from config_class import config
import requests



def get_and_push_plj_values(output, cust_id, isp_wan_id, internal_ip):

    isp_data = {}
    latencies = re.findall(r"time=(\d+(?:\.\d+)?)", output)
    packet_loss_match = re.search(r'(\d+(?:\.\d+)?)%\s+packet loss', output)
    if packet_loss_match is None:
        isp_data = {
                    "isp_wan_id": isp_wan_id,
                    "client_id": cust_id,
                    "circuit_id": "NA",
                    "public_ip": internal_ip,
                    "min_rtt": 0,
                    "avg_rtt": 0,
                    "max_rtt": 0,
                    "jitter": 0,
                    "packet_loss": 100,
                    "status": 0,
                    
                    "dg_ip": '0.0.0.0',
                    "dg_status": 1,
                    "dg_min_rtt": 0,
                    "dg_max_rtt": 0,
                    "dg_avg_rtt": 0,
                    "dg_jitter": 0,
                    "dg_packet_loss": 0,
                    "time": start_time
                }
    else:
        try:
            if latencies and packet_loss_match:
                packet_loss = packet_loss_match.group(1)
                latencies = [float(latency) for latency in latencies]
                avg_latency = sum(latencies) / len(latencies)

                squared_diff_sum = sum((latency - avg_latency) ** 2 for latency in latencies)
                jitter = (squared_diff_sum / len(latencies)) ** 0.5

                status = 1 if packet_loss != '100' else 0

                isp_data = {
                    "isp_wan_id": isp_wan_id,
                    "client_id": cust_id,
                    "circuit_id": "NA",
                    "public_ip": internal_ip,
                    "min_rtt": min(latencies),
                    "avg_rtt": avg_latency,
                    "max_rtt": max(latencies),
                    "jitter": jitter,
                    "packet_loss": packet_loss,
                    "status": status,
                    
                    "dg_ip": '0.0.0.0',
                    "dg_status": 1,
                    "dg_min_rtt": 0,
                    "dg_max_rtt": 0,
                    "dg_avg_rtt": 0,
                    "dg_jitter": 0,
                    "dg_packet_loss": 0,
                    "time": start_time
                }
            else:
                isp_data = {
                    "isp_wan_id": isp_wan_id,
                    "client_id": cust_id,
                    "circuit_id": "NA",
                    "public_ip": internal_ip,
                    "min_rtt": 0,
                    "avg_rtt": 0,
                    "max_rtt": 0,
                    "jitter": 0,
                    "packet_loss": 100,
                    "status": 0,
                    
                    "dg_ip": '0.0.0.0',
                    "dg_status": 1,
                    "dg_min_rtt": 0,
                    "dg_max_rtt": 0,
                    "dg_avg_rtt": 0,
                    "dg_jitter": 0,
                    "dg_packet_loss": 0,
                    "time": start_time
                }
        except Exception as e:
            isp_data = {
                    "isp_wan_id": isp_wan_id,
                    "client_id": cust_id,
                    "circuit_id": "NA",
                    "public_ip": internal_ip,
                    "min_rtt": 0,
                    "avg_rtt": 0,
                    "max_rtt": 0,
                    "jitter": 0,
                    "packet_loss": 100,
                    "status": 0,
                    
                    "dg_ip": '0.0.0.0',
                    "dg_status": 1,
                    "dg_min_rtt": 0,
                    "dg_max_rtt": 0,
                    "dg_avg_rtt": 0,
                    "dg_jitter": 0,
                    "dg_packet_loss": 0,
                    "time": start_time
                }
    # Push Data to core
    creds = config.creds
    server = config.server
    cust_id = config.client_id
    
    json_data = {
        "creds": creds,
        "isp_data": isp_data
    }
    print(json_data)
    try:

        api_path = server + "api/push_isp_data.php"
        # api_response = requests.post(api_path, json=json_data, verify=False)
        # print(api_response.json())
    except Exception as e:
        print("Error in Pushing Data", e)


def find_plj_for_Viptella_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port):
    
    command = f"ping 8.8.4.4 source {if_name} count 5"
   
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=4)

        channel = ssh.invoke_shell()
        time.sleep(1)
        sleep_time = 5

        output = ""
        
        channel.send(command + "\n")
        time.sleep(sleep_time)  # Wait for the command to execute
        while channel.recv_ready():
            output += channel.recv(1024).decode()

        get_and_push_plj_values(output, cust_id, isp_wan_id, internal_ip)

    except Exception as e:
        print("Error occured", e)
    finally:
        ssh.close()


def find_plj_for_meraki_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, device_serial, default_gateway, api_key, api_port):
    url = f"""https://api.meraki.com/api/v1/devices/{device_serial}/lossAndLatencyHistory"""
    payload = f"""ip=8.8.8.8&resolution=60&uplink={if_name}&timespan=300"""
    headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    
    response = requests.get(url, headers=headers, data=payload)
    data_arr = response.json()

    if len(data_arr) < 2:
        print(f"Error: Meraki Link ISP WAN ID: {isp_wan_id} Not Responding")
        return
    
    last_data = data_arr[-2]

    status = 1

    if last_data['lossPercent'] is None or last_data['lossPercent'] == 'NULL':
        return 


    if last_data['lossPercent'] == 100:
        status = 0
        last_data['latencyMs'] = 0
        last_data['jitter'] = 0


    isp_data = {
                "isp_wan_id": isp_wan_id,
                "client_id": cust_id,
                "circuit_id": "NA",
                "public_ip": internal_ip,
                "min_rtt": last_data['latencyMs'],
                "avg_rtt": last_data['latencyMs'],
                "max_rtt": last_data['latencyMs'],
                "jitter": last_data['jitter'],
                "packet_loss": last_data['lossPercent'],
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
        # api_response = requests.post(api_path, json=json_data, verify=False)
        # print(api_response.json())
    except Exception as e:
        print("Error in Pushing Data", e)

    pass


def find_plj_for_silverpeak_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port):
    
    command = f"ping -I {if_name} 8.8.4.4 -c 5"
   
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=4)

        channel = ssh.invoke_shell()
        time.sleep(1)
        sleep_time = 2

        output = ""
        channel.send("enable \n")
        time.sleep(sleep_time)
        channel.send(command + "\n")
        time.sleep(6)  # Wait for the command to execute
        while channel.recv_ready():
            output += channel.recv(1024).decode()
        
        print("Output", output)
        get_and_push_plj_values(output, cust_id, isp_wan_id, internal_ip)

    except Exception as e:
        print("Error occured", e)
    finally:
        ssh.close()


def get_plj_dbb_link(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port, vendor, type, device_serial, default_gateway, api_key, api_port):

    if vendor == 'Viptella':
        find_plj_for_Viptella_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port)
    if vendor == 'Fortinet':
        print("Code for Fortinet")
    if vendor == 'Meraki':
        find_plj_for_meraki_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, device_serial, default_gateway, api_key, api_port)
    if vendor == 'Silverpeak':
        find_plj_for_silverpeak_device_links(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port)

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
                WHERE fn_isp_details.link_type='DBB' AND fn_isp_details.edge_device_id=fn_edge_devices.device_id AND fn_isp_details.isp_wan_id=10674"""
    
    cursor.execute(dbb_links_sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    # Create processes for each device
    for row in result:
        print(row)
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


    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    # Print the summary
    now = datetime.datetime.now()
    end_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: DBB links polling Completed at:{end_time}")
