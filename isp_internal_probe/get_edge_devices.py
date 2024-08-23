import requests
import mysql.connector as connector
import pandas as pd
from config_class import config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def table_exists(cursor, table_name):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    return cursor.fetchone() is not None

if __name__ == "__main__":

    url= config.server + "api/get_edge_devices_by_client_v2_msp.php"
    print(url)
    #Payload
    data = {
        "creds": config.creds,
        "client_id": config.client_id
    }
    response = requests.post(url, headers=config.headers, json=data , verify=False)
    response_data = response.json()

    devices = []

    if response_data:
        devices = response_data['locations']
    else:
        print("No response from API")
        exit()

    try:
        conn = connector.connect(
            host=config.mysql_conf["host"],
            user=config.mysql_conf["user"],
            password=config.mysql_conf["password"],
            port=config.mysql_conf["port"],
            database=config.mysql_conf["database"],
            # auth_plugin=config.mysql_conf["auth_plugin"]
        )

        cursor = conn.cursor()

        # Check if table exists
        if not table_exists(cursor, 'fn_edge_devices'):
            # Create table if it doesn't exist
            create_table_sql = """
            CREATE TABLE fn_edge_devices (
                id INT AUTO_INCREMENT PRIMARY KEY,
                device_id INT NOT NULL,
                cust_id INT NOT NULL,
                location_id INT NOT NULL,
                location_name VARCHAR(255),
                device_ip VARCHAR(255),
                org_id VARCHAR(255),
                host_name VARCHAR(255),
                device_public_ip VARCHAR(255),
                device_serial VARCHAR(255),
                snmp_str VARCHAR(255),
                snmp_version TINYINT(3),
                security_level VARCHAR(255),
                auth_type VARCHAR(255),
                auth_password VARCHAR(255),
                privacy_type VARCHAR(255),
                privacy_password VARCHAR(255),
                ssh_username VARCHAR(255),
                ssh_password VARCHAR(255),
                api_key VARCHAR(255),
                ssh_port  VARCHAR(50),
                api_port  VARCHAR(50),
                vendor VARCHAR(50),
                type VARCHAR(50),
                ent DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_sql)

        for device in devices:
            device_id = device['device_id']
            cust_id = device['cust_id']
            location_id = device['location_id']
            location_name = device['location_name']
            device_ip = device['device_ip']
            snmp_str = device['snmp_str']
            ssh_username = device['ssh_username']
            ssh_password = device['ssh_password']
            api_key = device['api_key']
            ssh_port = device['ssh_port']
            api_port = device['api_port']
            device_vendor = device['device_vendor']
            device_type = device['type']
            org_id = device['org_id']
            host_name = device['host_name']
            device_public_ip = device['device_public_ip']
            device_serial = device['device_serial']
            snmp_version = device['snmp_version']
            security_level = device['security_level']
            auth_type = device['auth_type']
            auth_password = device['auth_password']
            privacy_type = device['privacy_type']
            privacy_password = device['privacy_password']

            
            try:
                delete_sql = f"DELETE FROM fn_edge_devices WHERE device_id={device_id}"
                cursor.execute(delete_sql)
                conn.commit()

                insert_sql = """INSERT INTO fn_edge_devices 
                                (device_id, cust_id, location_id, location_name, device_ip, snmp_str, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, ssh_username, ssh_password, api_key, ssh_port, api_port, vendor, type, org_id, host_name, device_public_ip, device_serial) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (device_id, cust_id, location_id, location_name, device_ip, snmp_str, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, ssh_username, ssh_password, api_key, ssh_port, api_port, device_vendor, device_type, org_id, host_name, device_public_ip, device_serial)
                cursor.execute(insert_sql, values)
                conn.commit()
                print(f"Inserted Device {device_ip} into Table")
            except Exception as err:
                print("Error in SQL Operation", err)
    except Exception as error:
        print("Error in SQL Operation", error)
    finally:
        cursor.close()
        conn.close()
