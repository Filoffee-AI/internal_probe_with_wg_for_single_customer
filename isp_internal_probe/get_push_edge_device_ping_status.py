import mysql.connector
import requests
from datetime import datetime
import json
import multiprocessing
import subprocess
from config_class import config
import logging

device_status = []

def get_db_connection():
    myconfig = {
        'host': config.mysql_conf["host"],
        'user': config.mysql_conf["user"],
        'password': config.mysql_conf["password"],
        'database': config.mysql_conf["database"],
        'auth_plugin': config.mysql_conf["auth_plugin"],
    }
    return mysql.connector.connect(**myconfig)

def get_device_ips():
    # try:
    #     data = {
    #         "creds": config.creds,
    #         "client_id": config.client_id,
    #     }
    #     print(data)
    #     api_path = config.server + "api/get_edge_devices_ips_by_client_msp.php"
    #     api_response = requests.get(api_path, json=data, verify=False)
    #     api_response.raise_for_status()
    #     response_json = api_response.json()

    #     code = response_json.get('code')
    #     if code == 1:
    #         client_id = response_json.get('client_id')
    #         device_data = response_json.get('device_data')
    #         return client_id, device_data

    # except Exception as e:
    #     logging.error(f'Error while calling data to API: {e}')
    # return None, []
    conn = get_db_connection()
    cursor = conn.cursor()

    select_devices_sql = "SELECT cust_id, device_id, device_ip FROM fn_edge_devices"
    cursor.execute(select_devices_sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result
    

def call_push_data(client_id, device_id, device_ip, creds, server ):
   cmd = [
        "python3",
        "push_ed_data_to_core.py",
        str(client_id),
        str(device_id),
        str(device_ip),
        str(creds['username']),
        str(creds['password']),
        str(server)
    ]
   subprocess.run(cmd)

def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Start Time:", current_time)

    creds = config.creds
    server = config.server
    devices = get_device_ips()

    process_list = []
    for ed in devices:
        cust_id = ed[0]
        device_id = ed[1]
        device_ip = ed[2].strip()

        process = multiprocessing.Process(target=call_push_data, args=(cust_id, device_id,  device_ip, creds, server))
        process_list.append(process)

    # Start each process
    for process in process_list:
        process.start()

    # Wait for all processes to finish
    for process in process_list:
        process.join()

    current_time = datetime.now().strftime("%H:%M:%S")
    print("Finished Time:", current_time)

if __name__ == "__main__":
    main()
