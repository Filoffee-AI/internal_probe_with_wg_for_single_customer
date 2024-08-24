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

    url= config.server + "api/get_isp_links_v2.php"

    #Payload
    data = {
        "creds": config.creds,
        "client_id": config.client_id
    }

    response = requests.post(url, headers=config.headers, json=data , verify=False)
    response_data = response.json()

    # print(response_data)

    links = []

    if response_data:
        links = response_data['data']
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
        
        if not table_exists(cursor, 'fn_isp_details'):
            # Create table if it doesn't exist
            create_table_sql = """
            CREATE TABLE `fn_isp_details` (
                `id` INT(10) NOT NULL AUTO_INCREMENT,
                `isp_wan_id` INT(10) NOT NULL DEFAULT '-1',
                `edge_device_id` INT(10) NOT NULL DEFAULT '0',
                `cust_id` INT(10) NULL DEFAULT '0',
                `location_id` INT(10) NULL DEFAULT NULL,
                `public_ip` VARCHAR(100) ,
                `private_ip` VARCHAR(100) ,
                `internal_ip` VARCHAR(100) ,
                `vendor_id` INT(10) NULL DEFAULT NULL,
                `default_gateway` VARCHAR(100) ,
                `firewall_ip` VARCHAR(100),
                `link_type` VARCHAR(50),
                `if_name` VARCHAR(50),
                `if_index` VARCHAR(50),
                `ent` DATETIME DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (`id`) USING BTREE
            );
            """
            cursor.execute(create_table_sql)

        if not table_exists(cursor, 'fn_latest_in_out_octates'):
            create_octate_table = """ 
            CREATE TABLE `fn_latest_in_out_octates` (
                `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
                `isp_wan_id` INT(10) UNSIGNED NULL DEFAULT NULL,
                `public_ip` VARCHAR(50) NULL DEFAULT NULL,
                `device_ip` VARCHAR(50) NULL DEFAULT NULL,
                `ifindex` SMALLINT(5) NULL DEFAULT NULL,
                `in_octates` BIGINT(20) UNSIGNED NULL DEFAULT NULL,
                `out_octates` BIGINT(20) UNSIGNED NULL DEFAULT NULL,
                `created_at` DATETIME DEFAULT 'CURRENT_TIMESTAMP',
                `updated_at` DATETIME DEFAULT 'CURRENT_TIMESTAMP' ON UPDATE CURRENT_TIMESTAMP,
                PRIMARY KEY (`id`) USING BTREE,
                INDEX `public_ip` (`public_ip`) USING BTREE,
                INDEX `device_ip` (`device_ip`) USING BTREE,
                INDEX `created_at` (`created_at`) USING BTREE,
                INDEX `isp_wan_id` (`isp_wan_id`) USING BTREE
            );
            """


        for link in links:
            isp_wan_id = link['isp_wan_id']
            cust_id = link['cust_id']
            location_id = link['location_id']
            public_ip = link['public_ip']
            private_ip = link['private_ip']
            internal_ip = link['internal_ip']
            vendor_id = link['vendor_id']
            default_gateway = link['default_gateway']
            firewall_ip = link['firewall_ip']
            link_type = link['link_type']
            if_name = link['if_name']
            if_index = link['if_index']
            device_id = link['device_id']

            try:
                delete_sql = f"DELETE FROM fn_isp_details WHERE isp_wan_id={isp_wan_id}"
                cursor.execute(delete_sql)
                conn.commit()

                insert_sql = f"""INSERT INTO `fn_isp_details` (`isp_wan_id`, `cust_id`, `location_id`, `edge_device_id`, `public_ip`, `private_ip`, `internal_ip`, `vendor_id`, `default_gateway`, `firewall_ip`, `link_type`, `if_name`, `if_index`) 
                                VALUES ('{isp_wan_id}', '{cust_id}', '{location_id}','{device_id}', '{public_ip}', '{private_ip}', '{internal_ip}', '{vendor_id}', '{default_gateway}', '{firewall_ip}', '{link_type}', '{if_name}', '{if_index}')"""
                # print(insert_sql)
                cursor.execute(insert_sql)
                conn.commit()
            except Exception as err:
                print("Error in Sql Operation", err)
    except Exception as error:
        print("Error in Sql Operation", error)
    finally:
        cursor.close()
        conn.close()
