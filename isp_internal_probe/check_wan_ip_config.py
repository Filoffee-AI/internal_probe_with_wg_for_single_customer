import sys
import json
import mysql.connector
import subprocess
from config_class import config
import re


def escape_special_characters(string):
    escaped_string = re.sub(r"([\\\"\n\r])", r"\\\1", string)
    return escaped_string


fw_ip = sys.argv[1].strip()
wan_ip = sys.argv[3].strip()

if __name__ == "__main__":

    conn = mysql.connector.connect(
        host=config.mysql_conf["host"],
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        port=config.mysql_conf["port"],
        database=config.mysql_conf["database"],
        auth_plugin=config.mysql_conf["auth_plugin"]
    )
    cursor = conn.cursor()

    fw_qry = f"select distinct(snmp_str) from link_det WHERE device_ip='{fw_ip}'"
    cursor.execute(fw_qry)
    fw_results = cursor.fetchall()
    if len(fw_results) > 0:
        for row in fw_results:
            snmp_str = escape_special_characters(row[0])

    process = subprocess.Popen(f"""snmpwalk -v2c -c {snmp_str} {fw_ip} RFC1213-MIB::ipAdEntIfIndex | grep {wan_ip} | 
    cut -d ':' -f 4""", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"""snmpwalk -v2c -c {snmp_str} {fw_ip} RFC1213-MIB::ipAdEntIfIndex | grep {wan_ip} | 
    cut -d ':' -f 4""")
    output, error = process.communicate()
    ifindex = output.decode('utf-8').strip()
    wan_dict = {}

    # main_dict = {}
    wan_dict = {}
    if ifindex == "":
        wan_dict['wan_code'] = -1
        wan_dict['wan_message'] = "WAN IP is not configured"
    else:
        query = f"SELECT * FROM link_det WHERE public_ip='{wan_ip}' AND ifindex='{ifindex}'"
        # print(query)
        cursor.execute(query)
        results = cursor.fetchall()

        if len(results) > 0:
            wan_dict['wan_code'] = 1
            wan_dict['wan_message'] = "WAN IP is configured"
        else:
            wan_dict['wan_code'] = -1
            wan_dict['wan_message'] = "WAN IP is not configured"

    # main_dict['wan'] = wan_dict
    print(json.dumps(wan_dict))
