import mysql.connector
import subprocess
from config_class import config
import datetime
import multiprocessing
from multiprocessing import Manager
import subprocess
import paramiko
import time
import re
import json
from paramiko.ssh_exception import AuthenticationException



def clean_data_silverpeak(data):
    lines = data.split('\n')
    dash_index = next(i for i, line in enumerate(lines) if '--------' in line) + 1
    vedge_index = len(lines) - next(i for i, line in enumerate(reversed(lines)) if '#' in line) - 1
    filtered_lines = lines[dash_index:vedge_index]
    result = '\n'.join(filtered_lines)
    return result

def find_interfaces_for_silverpeak(data):
    pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)\s+(\S+)\s+(\S+)")

    # Define the keys for each captured group
    keys = ["IP_ADDRESS", "INTERFACE", "STATUS"]

    # Parse the data
    interfaces = []
    for match in pattern.finditer(data):
        row = {key: value.strip() for key, value in zip(keys, match.groups())}
        interfaces.append(row)

    return interfaces

def run_snmpwalk(host, community):
    command = ['snmpwalk', '-v', '2c', '-c', community, host, "IF-MIB::ifDescr"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.returncode, result.stdout
    else:
        return result.returncode, f"Error: {result.stderr}"


def find_interfaces_for_silverpeak_host(device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, cust_id, successful_ips, failed_ipsy):
    
    print(device_ip)
    conn = mysql.connector.connect(
        host=config.mysql_conf["host"],
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        port=config.mysql_conf["port"],
        database=config.mysql_conf["database"],
        auth_plugin=config.mysql_conf["auth_plugin"]
    )
    cursor = conn.cursor()
    
    command = f"show system wan-next-hops"
   
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=4)

        channel = ssh.invoke_shell()
        time.sleep(1)
        sleep_time = 2

        output = ""
        channel.send("enable" + "\n")
        time.sleep(sleep_time)
        
        channel.send(command + "\n")
        time.sleep(sleep_time)  # Wait for the command to execute
        while channel.recv_ready():
            output += channel.recv(1024).decode()
        
        all_interfaces = find_interfaces_for_silverpeak(clean_data_silverpeak(output))
        reachable_interfaces = [d for d in all_interfaces if d["IP_ADDRESS"] != "0.0.0.0" and d["STATUS"] == "reachable"]

        for ri in reachable_interfaces:
            output = ""
            int_face = ri['INTERFACE']

            command = f"show interfaces {int_face}"
            channel.send(command + "\n")
            time.sleep(sleep_time)  # Wait for the command to execute
            while channel.recv_ready():
                output += channel.recv(1024).decode()
            
            pattern = r'IP address:\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            match = re.search(pattern, output)
            
            # Extracting the IP address if found
            ip_address = match.group(1) if match else None

            if ip_address is not None:
                ri['IP_ADDRESS'] = ip_address
        
        snmp_code, snmp_data = run_snmpwalk(device_ip, snmp_str)
        if snmp_code != 0:
            print("Error in snmp", snmp_data)
            exit

        snmp_desc_dict = {}
        for line in snmp_data.splitlines():
            match = re.search(r"IF-MIB::ifDescr\.(\d+) = STRING: (.+)$", line)
            if match:
                if_index, if_name = match.groups()
                snmp_desc_dict[if_name] = if_index
        
        for interface in reachable_interfaces:
            if_name = interface['INTERFACE']
            if if_name in snmp_desc_dict:
                interface['IF_INDEX'] = snmp_desc_dict[if_name]
        

        isp_sql = f"SELECT isp_wan_id, internal_ip FROM fn_isp_details WHERE location_id='{location_id}'"
        cursor.execute(isp_sql)
        isps = cursor.fetchall()
        for isp in isps:
            isp_wan_id = isp[0]
            ip = isp[1]
            print("ip", ip)
            macthed_if_arr =  [d for d in reachable_interfaces if ip == d["IP_ADDRESS"]]
            print("isp_wan_id", isp_wan_id)
            print(macthed_if_arr)
            if len(macthed_if_arr) > 0:
                if_obj = macthed_if_arr[0]
                if_name = if_obj['INTERFACE']
                if_index = if_obj['IF_INDEX']
                update_if_det_sql = f"UPDATE `fn_isp_details` SET `if_name`='{if_name}', `if_index`='{if_index}', `edge_device_id`='{device_id}' WHERE `isp_wan_id`='{isp_wan_id}'"
                cursor.execute(update_if_det_sql)
                conn.commit()
                reachable_interfaces = [d for d in reachable_interfaces if ip not in d["IP_ADDRESS"]]
        
        for interface in reachable_interfaces:
            if_name = interface['INTERFACE']
            if_index = interface['IF_INDEX']
            ip_address = interface['IP_ADDRESS']

            insert_ip_sql = f"""INSERT INTO `fn_isp_details` (`isp_wan_id`, `edge_device_id`, `cust_id`, `location_id`, `public_ip`, `private_ip`, `internal_ip`, `vendor_id`, `default_gateway`, `firewall_ip`, `link_type`, `if_name`, `if_index`) 
                                                        VALUES ('-1', '{device_id}', '{cust_id}', '{location_id}', '{ip_address}', 'None', '{ip_address}', '-1', '0.0.0.0', '{device_ip}', 'DBB', '{if_name}', '{if_index}')"""
            cursor.execute(insert_ip_sql)
            conn.commit()
        
    except AuthenticationException:
        print(f"{device_ip} Authentication failed. Please check your credentials.")
    except Exception as ex:
        print(f"{device_ip} An error occurred: {str(ex)}")

    finally:
        ssh.close()
        cursor.close()
        conn.close()


def update_ifindex(device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, vendor, type, cust_id, successful_ips, failed_ips):

    if vendor == 'Viptella':
        print("Code for Viptella")
    if vendor == 'Fortinet':
        print("Code for Fortinet")
    if vendor == 'Silverpeak':
        find_interfaces_for_silverpeak_host(device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, cust_id, successful_ips, failed_ips)

    return


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

    now = datetime.datetime.now()
    start_time = now.strftime("%d-%m-%Y %H:%M:%S")
    
    successful_ips = Manager().list()
    failed_ips = Manager().list()

    process_list = []

    device_sql = "SELECT device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, vendor, type, cust_id FROM fn_edge_devices WHERE device_id=1097"
    cursor.execute(device_sql)
    result = cursor.fetchall()
    

    # Create processes for each device
    for row in result:
        device_id = row[0]
        device_ip = row[1]
        location_id = row[2]
        snmp_str  = row[3]
        ssh_username = row[4]
        ssh_password = row[5]
        ssh_port = row[6]
        vendor = row[7]
        type = row[8]
        cust_id = row[9]
        process = multiprocessing.Process(target=update_ifindex, args=(device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, vendor, type, cust_id, successful_ips, failed_ips,))
        process_list.append(process)

    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    # Print the summary

    cursor.close()  
    conn.close()


    total_ips = len(successful_ips) + len(failed_ips)
    now = datetime.datetime.now()
    end_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: SNMP Walk Completed at:{end_time}")
