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


def main():
    conn = get_db_connection()
    cursor = conn.cursor()
    isp_sql = f"""SELECT id, isp_wan_id, edge_device_id, cust_id, location_id, public_ip, private_ip, internal_ip, vendor_id, default_gateway, firewall_ip, link_type, if_name, if_index FROM fn_isp_details WHERE edge_device_id != 0"""
    
    cursor.execute(isp_sql)
    isp_res = cursor.fetchall()

    data_list = [
        {   
            "id": id,
            "isp_wan_id": isp_wan_id, 
            "device_id": edge_device_id,
            "cust_id": cust_id,
            "location_id": location_id,
            "public_ip": public_ip,
            "private_ip": private_ip,
            "internal_ip": internal_ip,
            "vendor_id": vendor_id,
            "default_gateway": default_gateway,
            "firewall_ip": firewall_ip,
            "link_type": link_type,
            "if_name": if_name,
            "if_index": if_index
        }
        for id, isp_wan_id, edge_device_id, cust_id, location_id, public_ip, private_ip, internal_ip, vendor_id, default_gateway, firewall_ip, link_type, if_name, if_index in isp_res
    ]

    try:
        payload = {
            "creds": config.creds,
            "cust_id": config.client_id,
            "dbb_link_arr": data_list
        }

        api_path = config.server + "api/push_link_data_for_msp.php"

        print(payload)
        api_response = requests.post(api_path, json=payload, verify=False)
        api_response.raise_for_status()
        response = api_response.json()
        dbb_links = response['dbb_links']
        for link in dbb_links:
            print(link)
            id = link['id']
            isp_wan_id = link['isp_wan_id']
            # cust_id = resp['cust_id']
            # location_id = resp['location_id']
            # internal_ip = resp['internal_ip']
            # link_type = resp['link_type']

            update_sql = f"""UPDATE fn_isp_details SET isp_wan_id={isp_wan_id} WHERE id={id}"""
            cursor.execute(update_sql)
            conn.commit()

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
    except Exception as e:
        logging.error(f'Error while pushing data to API: {e}')
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
