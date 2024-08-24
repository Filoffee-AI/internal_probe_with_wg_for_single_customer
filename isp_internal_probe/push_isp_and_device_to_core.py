from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import mysql.connector
import requests
from config_class import config
import logging

def get_db_connection():
    myconfig = {
        'host': config.mysql_conf["host"],
        'user': config.mysql_conf["user"],
        'password': config.mysql_conf["password"],
        'database': config.mysql_conf["database"],
    }
    return mysql.connector.connect(**myconfig)


def send_isp_ed_data_to_core(data):
    try:
        payload = {
            "creds": config.creds,
            "cust_id": config.client_id,
            "link_device_arr": data
        }
        # print(payload)
        api_path = config.server + "api/push_isp_link_ifindex.php"

        api_response = requests.post(api_path, json=payload, verify=False)

        api_response.raise_for_status()
        print(api_response.json())
    except Exception as e:
        logging.error(f'Error while pushing data to API: {e}')

def main():
    conn = get_db_connection()
    cursor = conn.cursor()
    ed_sql = f"""SELECT 
                    fn_isp_details.isp_wan_id,
                    fn_isp_details.public_ip,
                    fn_edge_devices.device_id,
                    fn_edge_devices.device_ip,
                    fn_edge_devices.location_id
                FROM fn_edge_devices, fn_isp_details 
                WHERE fn_edge_devices.device_id=fn_isp_details.edge_device_id AND fn_isp_details.if_index IS NOT NULL"""
    
    cursor.execute(ed_sql)
    ed_res = cursor.fetchall()
    cursor.close()
    conn.close()

    # Modify the data to be a list of dictionaries
    data_list = [
        {
            "location_id": location_id,
            "isp_wan_id": isp_wan_id,
            "public_ip": public_ip,
            "device_id": device_id,
            "device_ip": device_ip
        }
        for isp_wan_id, public_ip, device_id, device_ip, location_id in ed_res
    ]

    # Use ThreadPoolExecutor for database fetching which is I/O bound
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.submit(send_isp_ed_data_to_core, data_list)


if __name__ == "__main__":
    main()
