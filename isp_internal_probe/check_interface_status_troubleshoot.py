import mysql.connector
import json
import sys
sys.path.append('../')
from config_class import config
import subprocess

''' Vendor types:
vendor_id | vendor_name
    2      | Fortinet  
    3      | Aruba  
    4      | SOPHOS  
    6      | Cisco  
    7      | Versa  
    9      | Lavelle  
    10     | Meraki  
    11     | Mist
    12     | Silverpeak  
    13     | Vyptella  
    14     | Palo Alto 
'''

def get_interface_status(isp_wan_id):
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
                  
        snmp_string = result[0]
        device_ip = result[1]
        ifindex = result[2]

        if ifindex is not None:
            cmd = ["snmpwalk", "-v2c", "-c", snmp_string, device_ip, f"1.3.6.1.2.1.2.2.1.8.{ifindex}"]
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
    response_dict = {}
    isp_wan_id = sys.argv[1]
    vendor_id = sys.argv[2]

    if vendor_id == 2 or vendor_id == 3 or vendor_id == 12 or vendor_id == 13 or vendor_id == 6 or vendor_id == 14:
        interface_status = get_interface_status(isp_wan_id)
    elif vendor_id == 10:
        interface_status = get_interface_status(isp_wan_id)
    else:
        interface_status = get_interface_status(isp_wan_id)
    
    if interface_status == 1:
        response_dict['status'] = 1
    else:
        response_dict['status'] = -1
    
    print(json.dumps(response_dict))