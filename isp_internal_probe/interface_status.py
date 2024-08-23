import mysql.connector
import json
import os
import sys
import pytz
from datetime import datetime, timedelta
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from config_class import config
import subprocess

try:
    # def get_ifindex(public_ip):
    #     conn = mysql.connector.connect(
    #     user=config.mysql_conf["user"],
    #         password=config.mysql_conf["password"],
    #         host=config.mysql_conf["host"],
    #         database=config.mysql_conf["database"],
    #         auth_plugin='mysql_native_password'
    #     )
    #     cursor = conn.cursor()

    #     cursor.execute("""SELECT public_ip, ifindex FROM link_det""")
    #     result = cursor.fetchall()

    #     ifindex = None
    #     for ips in result:
    #         pu_ip = ips[0]
    #         index = ips[1]
    #         if public_ip == pu_ip and index != 'None':
    #             ifindex = index
    #             break

    #     cursor.close()
    #     conn.close()
    #     return ifindex


    def get_int_status(public_ip,isp_wan_id):
        try:
            conn = mysql.connector.connect(
            user=config.mysql_conf["user"],
            password=config.mysql_conf["password"],
                host=config.mysql_conf["host"],
                database=config.mysql_conf["database"],
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()

            cursor.execute("""SELECT fn_edge_devices.snmp_str, fn_edge_devices.device_ip, fn_isp_details.if_index FROM fn_edge_devices, fn_isp_details WHERE fn_edge_devices.device_id=fn_isp_details.edge_device_id AND fn_isp_details.isp_wan_id = '{}';""".format(isp_wan_id))
            result = cursor.fetchone()

            if result is None:
                return 0

            device_ip = result[1]        
            community_string = result[0]
            ifindex = result[2]
            if ifindex is not None:
                cmd = ["snmpwalk", "-v2c", "-c", community_string, device_ip, f"1.3.6.1.2.1.2.2.1.8.{ifindex}"]
                output = subprocess.run(cmd, stdout=subprocess.PIPE)
                device_output = output.stdout.decode('utf-8')

                if "INTEGER: up" in device_output:
                    status = 1
                else:
                    status = 0

                return status
            else:
                return 0
                
            
        except Exception as e:
            return 0
            



    if __name__ == '__main__':
        try: 
            device_ip = sys.argv[1]
            public_ip = sys.argv[2]
            isp_wan_id = sys.argv[3]
            response_dict = {}
            int_status = get_int_status(public_ip, isp_wan_id)
            
            if int_status == 1:
                response_dict['status'] = 1
                response_dict['message'] = f"WAN Interface on the Customer Equipment(CE) is UP"
            else:
                response_dict['status'] = -1
                response_dict['rca_message'] = f"WAN Interface on the Customer Equipment(CE) is Down"
                response_dict['message'] = f"WAN Interface on the Customer Equipment(CE) is Down. Check if WAN IP(CE-IP) is Configured on the Interface. Please Reach Out to the Site Contact to Check the Following : \n a. Is the Modem/ISP router/ONT powered on and connecting \n b. Is the Modem/ISP router LED lights Green \n c. Check the Fibre connection to the ISP box \n d.Check the Wired Connection to the Firewall"
        except Exception as e:
                response_dict = {}
                response_dict['status'] = -1
                response_dict['rca_message'] = f"WAN Interface on the Customer Equipment(CE) is Down"
                response_dict['message'] = f"WAN Interface on the Customer Equipment(CE) is Down"

        print(json.dumps(response_dict))

except Exception as e:
    response_dict = {}
    response_dict['status'] = -1
    response_dict['rca_message'] = f"Failed to Check WAN Interface Status"
    response_dict['message'] = f"Failed to Check WAN Interface Status"

    print(json.dumps(response_dict))