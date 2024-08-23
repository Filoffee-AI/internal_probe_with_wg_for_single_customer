from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from easysnmp import Session, exceptions as easysnmp_exceptions
import mysql.connector
from datetime import datetime
from config_class import config
import subprocess
import requests
import json

host = config.mysql_conf["host"]
database = config.mysql_conf["database"]
user = config.mysql_conf["user"]
password = config.mysql_conf["password"]
port = config.mysql_conf["port"]
auth_plugin = config.mysql_conf["auth_plugin"]

config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database,
    'port': port,
    'auth_plugin': auth_plugin
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()


def pull_isp_data(org_id, api_key):

    url = f"""https://api.meraki.com/api/v1/organizations/{org_id}/devices/uplinks/addresses/byDevice"""
    headers = {
        'Authorization': f'Bearer {api_key}'
        }
    response = requests.get(url, headers=headers)
    devices_dict = {}
    devices = response.json()
    for device in devices:
        serial = device['serial']
        devices_dict[serial] = device 
    
    devices_sql = f"""SELECT device_id, location_id, device_serial, device_ip, device_public_ip, cust_id
                        FROM fn_edge_devices WHERE vendor='Meraki' AND org_id='{org_id}' AND device_id='1165'"""
    cursor.execute(devices_sql)

    devices = cursor.fetchall()

    for device in devices:
        device_id = device[0]
        location_id = device[1]
        device_serial = device[2]
        device_public_ip = device[4]
        cust_id = device[5]
        
        if device_serial in devices_dict:
            device_dict = devices_dict[device_serial]
        else:
            continue
        
        links = device_dict['uplinks']
        print(links)

        for link in links:
            interface = link['interface']
            addresses = link['addresses']

            if "wan" in interface and len(addresses)>0:
                if_name = interface
                if_index = int(interface.replace("wan", ""))

                ipv4addrs = [d for d in addresses if d['protocol'] == 'ipv4'] 
                addr = ipv4addrs[0]

                link_ip = addr['address']
                gateway = addr['gateway']

                public_addr = addr['public']
                public_ip = public_addr['address']

                check_public_ip_sql = f"""SELECT isp_wan_id FROM fn_isp_details WHERE location_id='{location_id}' AND internal_ip='{link_ip}'"""
                print(check_public_ip_sql)
                cursor.execute(check_public_ip_sql)
                res = cursor.fetchall()

                if len(res) > 0:
                    row = res[0]
                    isp_wan_id = row[0]
                    update_sql = f"UPDATE fn_isp_details SET edge_device_id='{device_id}', if_name='{if_name}', if_index='{if_index}' WHERE isp_wan_id={isp_wan_id}"
                    cursor.execute(update_sql)
                    conn.commit()
                    continue 


                is_exist_sql = f"""SELECT * FROM fn_isp_details WHERE edge_device_id='{device_id}' AND if_name='{if_name}'"""
                print(is_exist_sql)
                cursor.execute(is_exist_sql)

                res = cursor.fetchall()

                if len(res) > 0:
                    update_sql = f"""UPDATE fn_isp_details SET public_ip='{public_ip}', internal_ip='{link_ip}', default_gateway='{gateway}' 
                                   WHERE  edge_device_id='{device_id}' AND if_name='{if_name}'"""
                    print(update_sql)
                    cursor.execute(update_sql)
                    conn.commit()
                else:
                    insert_sql = f"""INSERT INTO `fn_isp_details` (`isp_wan_id`, `edge_device_id`, `cust_id`, `location_id`, `public_ip`, `private_ip`, `internal_ip`, `vendor_id`, `default_gateway`, `firewall_ip`, `link_type`, `if_name`, `if_index`) 
						VALUES ('-1', {device_id}, {cust_id}, {location_id}, '{public_ip}', 'None', '{link_ip}', -1, '{gateway}', '{device_public_ip}', 'DBB', '{if_name}', '{if_index}')"""
                    cursor.execute(insert_sql)
                    conn.commit()
    return


if __name__ == "__main__":
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Start Time:", current_time)

    org_list_sql = """SELECT org_id, api_key FROM fn_edge_devices 
                        WHERE vendor='Meraki' AND org_id IS NOT NULL AND org_id!='' AND org_id != 'None' GROUP BY org_id, api_key"""
    cursor.execute(org_list_sql)

    orgs = cursor.fetchall()

    if len(orgs) == 0:
        cursor.close()
        conn.close()
        exit(0)
    
    for org in orgs:
        org_id = org[0]
        api_key = org[1]
        pull_isp_data(org_id, api_key)

    current_time = now.strftime("%H:%M:%S")
    print("End Time:", current_time)
    cursor.close()
    conn.close()
    
