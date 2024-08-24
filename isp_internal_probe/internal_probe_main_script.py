import json
import multiprocessing
import requests
import datetime
import os
from config_class import config


def call_push_data(isp_wan_id, cust_id, circuit_id, location, isp_public_ip, vendor, creds, server, dg_ip):
    cmd = f'''python3 internal_push_data_to_core_using_ping_cmd.py "{isp_wan_id}" "{cust_id}" "{circuit_id}" "{location}" "{isp_public_ip}" "{vendor}" "{server}" "{creds['username']}" '{creds["password"]}' "{dg_ip}"'''
    os.system(cmd)


if __name__ == "__main__":

    creds = config.creds
    server = config.server
    cust_id = config.client_id

    json_data = {
        'creds': creds,
        'cust_id': cust_id
    }
    # print(json_data)
    api_path = server + "api/get_p2p_mtls_public_ips_by_customer.php"
    api_response = requests.post(api_path, json=json_data, verify=False)
    isp_arr = api_response.json()['isp_data']
    # print(isp_arr)
    now = datetime.datetime.now()
    start_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: Datapolling Started at:{start_time}")

    process_list = []
    for isp in isp_arr:
        isp_wan_id = isp['isp_wan_id']
        cust_id = isp['cust_id']
        circuit_id = isp['circuit_id'].strip()
        location = isp['location'].strip()
        public_ip = isp['public_ip'].strip()
        vendor = isp['vendor'].strip()
        dg_ip = isp['default_gateway'].strip()

        process = multiprocessing.Process(target=call_push_data, args=(isp_wan_id, cust_id, circuit_id, location, public_ip, vendor,creds,server,dg_ip,))
        process_list.append(process)

    # Start each process
    for process in process_list:
        process.start()

    # Wait for all processes to finish
    for process in process_list:
        process.join()

    now = datetime.datetime.now()
    start_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: Datapolling Completed at:{start_time}")
