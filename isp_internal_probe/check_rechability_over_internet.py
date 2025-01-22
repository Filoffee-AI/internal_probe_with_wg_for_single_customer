#!/usr/bin/env python3
import requests
import warnings
import sys
import json
import re
import subprocess
from config_class import config
import mysql.connector
warnings.filterwarnings('ignore')

dict = {}

def get_snmp_str(device_id, isp_wan_id):
    conn = mysql.connector.connect(
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        host=config.mysql_conf["host"],
        database=config.mysql_conf["database"],
        auth_plugin='mysql_native_password'
    )
    cursor = conn.cursor()

    try:
        cursor.execute("""SELECT device_ip, snmp_str FROM fn_edge_devices WHERE device_id=%s""", (device_id,))
        result = cursor.fetchone()
        fw_ip, snmp_str = result if result else (None, None)

        cursor.fetchall()

        cursor.execute("""SELECT internal_ip FROM fn_isp_details WHERE isp_wan_id=%s""", (isp_wan_id,))
        wan_result = cursor.fetchone()
        wan_ip = wan_result[0] if wan_result else None

        return wan_ip, fw_ip, snmp_str
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None, None, None

    finally:
        cursor.close()
        conn.close()

def run_snmp_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()
        return output.decode().strip()
    except Exception as e:
        print(f"Error running command {command}: {e}")
        return ""

def fetch_snmp_value(fw_ip, oid, match_pattern):
    command = f"snmpwalk -v2c -c '{snmp_str}' {fw_ip} {oid}"
    output = run_snmp_command(command)
    match = re.search(match_pattern, output)
    return match.group(1) if match else None

def check_internet_status_for_fortinet(fw_ip, wan_ip):
    if_index = fetch_snmp_value(fw_ip, f"ipAdEntIfIndex.{wan_ip}", r'INTEGER: (\d+)')
    if if_index:
        if_name = fetch_snmp_value(fw_ip, f"ifName.{if_index}", r'STRING: (.+)')
        if if_name:
            link_if_number = fetch_snmp_value(fw_ip, "fgVWLHealthCheckLinkTable", rf'FORTINET-FORTIGATE-MIB::fgVWLHealthCheckLinkIfName\.(\d+)')
            if link_if_number:
                link_state = fetch_snmp_value(fw_ip, f"fgVWLHealthCheckLinkState.{link_if_number}", r'\((\w+)\)')
                if link_state == "0" :
                    return  1, "Internet is Reachable"
                else:
                    return 0, "Internet is Not Reachable"
    return -1 , "Internet is Not Reachable"

if __name__ == "__main__":
    vendor_id = sys.argv[1].strip()
    isp_wan_id = sys.argv[2].strip()
    device_id = sys.argv[3].strip()

    wan_ip, fw_ip, snmp_str = get_snmp_str(device_id, isp_wan_id)
    response_dict = {}  

    if wan_ip and fw_ip and snmp_str:
        if vendor_id == "2":
            status, message = check_internet_status_for_fortinet(fw_ip, wan_ip)
        else:
            status, message = 1, "Internet is Reachable"


    response_dict['message'] = message
    response_dict['code'] = status
    print(json.dumps(response_dict))
