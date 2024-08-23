import mysql.connector
import json
from config_class import config
import datetime
import multiprocessing
from multiprocessing import Manager
import paramiko
import time
import re
from paramiko.ssh_exception import AuthenticationException
from config_class import config
import requests

def push_public_ip_and_vendor_data(cust_id, isp_wan_id, public_ip):

    conn = mysql.connector.connect(
        host=config.mysql_conf["host"],
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        port=config.mysql_conf["port"],
        database=config.mysql_conf["database"],
        auth_plugin=config.mysql_conf["auth_plugin"]
    )
    cursor = conn.cursor()

    creds = config.creds
    server = config.server
    
    json_data = {
        "creds": creds,
        "isp_info": {
            "cust_id": cust_id,
            "isp_wan_id": isp_wan_id,
            "public_ip": public_ip
        }
    }
    try:
        api_path = server + "api/push_public_ip_of_isp.php"
        api_response = requests.post(api_path, json=json_data, verify=False)
        ret_val = api_response.json()

        if ret_val['code'] == 1:
            update_sql = f"UPDATE fn_isp_details SET public_ip='{public_ip}' WHERE isp_wan_id='{isp_wan_id}'"
            cursor.execute(update_sql)
            conn.commit()
            print("Public IP updated for isp_wan_id", isp_wan_id)
    except Exception as e:
        print("Error in Pushing Data", e)
    cursor.close()
    conn.close()


def get_and_public_ip_and_vendor(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port):
    
    if_name_revised = if_name.replace('/', '_')
    command = f"curl --interface {if_name_revised} 'http://api.ipify.org?format=json'"
   
    try:
        sleep_time = 2
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=4)

        channel = ssh.invoke_shell()
        time.sleep(sleep_time)

        output = ""
        
        channel.send("vshell" + "\n")
        time.sleep(sleep_time)  # Wait for the command to execute
        channel.send(command + "\n")
        time.sleep(sleep_time)
        while channel.recv_ready():
            output += channel.recv(1024).decode()

        matches = re.findall(r'\{"ip":"(?:\d{1,3}\.){3}\d{1,3}"\}', output)
        if matches is not None and len(matches)>0:
            ip_dict = json.loads(matches[0])
            public_ip = ip_dict['ip']
            print("Public IP is", public_ip)

            # try:
            #     vendor_url = f"http://ip-api.com/json/{public_ip}"
            #     response = requests.get(vendor_url)
            #     vendor_data = response.json()
            #     
            # except Exception as e:
            #     print("Error in pull public ip and vendor")
            
            push_public_ip_and_vendor_data(cust_id, isp_wan_id, public_ip)
    except Exception as e:
        print("Error occured", e)
    finally:
        ssh.close()

def getInterAllfacesByAPI():
    base_url = "https://titan-orch-apsouth1.silverpeak.cloud/gms/rest/"
    login_url = base_url+"authentication/login"

    payload = json.dumps({
        "user": "Sushant",
        "password": "Link-eye_2024",
        "token": None,
        "tempCode": None
    })

    headers = {
        'Content-Type': 'application/json'
    }

    
    response = requests.post(login_url, headers=headers, data=payload)
    http_code = response.status_code
    
    if response.status_code == 200:
        cookies = requests.utils.dict_from_cookiejar(response.cookies)
        gmsSessionID = cookies.get('gmsSessionID', '')
        orchCsrfToken = cookies.get('orchCsrfToken', '')
        print("Session Id", gmsSessionID)
        print("orchCsrfToken Id", orchCsrfToken)

        if gmsSessionID and orchCsrfToken:
            cookie_header = f"gmsSessionID={gmsSessionID}; orchCsrfToken={orchCsrfToken}"
            headers = {
                'Content-Type': 'application/json',
                'Cookie': cookie_header
            }

            interface_url = base_url + "tunnelsConfiguration/deployment?source=menu_rest_apis_id?source=menu_rest_apis_id"
            interface_resp = requests.get(interface_url, headers=headers)
            print(interface_resp)
            if interface_resp.status_code == 200:
                print(interface_resp.json)

    return


def update_public_ip_and_vendor(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port, vendor, type):
    if vendor == 'Viptella':
        get_and_public_ip_and_vendor(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port)
    if vendor == 'Fortinet':
        print("Code for Fortinet")
    if vendor == 'Meraki':
        print("Code for Meraki")
    if vendor == 'Silverpeak':
        print("Code for Meraki")

    return


if __name__ == "__main__":

    # silverpeak_interface_list = getInterAllfacesByAPI()


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
                            fn_edge_devices.`type`			
                FROM fn_isp_details, fn_edge_devices
                WHERE fn_isp_details.link_type='DBB' AND fn_isp_details.edge_device_id=fn_edge_devices.device_id"""
    
    cursor.execute(dbb_links_sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    # Create processes for each device
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
        
        process = multiprocessing.Process(target=update_public_ip_and_vendor, args=(cust_id, isp_wan_id, internal_ip, if_name, if_index, device_id, device_ip, ssh_username, ssh_password, ssh_port, vendor, type))
        process_list.append(process)


    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    # Print the summary
    now = datetime.datetime.now()
    end_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: DBB links polling Completed at:{end_time}")
