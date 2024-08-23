import mysql.connector
import subprocess
from config_class import config
import datetime
import multiprocessing
from multiprocessing import Manager
import re

def check_interface_name(device_ip, ssh_username, ssh_password, ssh_port, gateway_ip):
    ip_arr = gateway_ip.split('.')
    network_address = '.'.join(ip_arr[:3])
    try:
        device_cmd = [
            "sshpass", "-p", ssh_password,
            "ssh", "-o", "StrictHostKeyChecking=no", "-p", str(ssh_port),
            f"{ssh_username}@{device_ip}",
            f"show ip route connected | include {network_address}"
        ]
       
        device_output = subprocess.run(device_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True, timeout=20)
        interface_op = device_output.stdout
        # print(interface_op)
        interface_match = re.search(fr'C\s+({network_address}\.\d+/\d+)\s+is directly connected, (.+)', interface_op, re.MULTILINE)
        if interface_match:
            network = interface_match.group(1)
            interface_name = interface_match.group(2)
            print(f"Inteface Name: {interface_name}")
            return interface_name
        else:
            print("Inteface Name not found.")
            return ""

    except subprocess.CalledProcessError:
        print("Failed to execute Device IP command in find_gateway")
        return ""  
    except subprocess.TimeoutExpired:
        print("Device IP  command timed out from find_gateway")
        return ""
    
def get_ip_from_interface_name(device_ip, ssh_username, ssh_password, ssh_port, interface_name):
    try:
        device_cmd = [
            "sshpass", "-p", ssh_password,
            "ssh", "-o", "StrictHostKeyChecking=no", "-p", str(ssh_port),
            f"{ssh_username}@{device_ip}",
            f"show ip int brief {interface_name}"
        ]
       
        device_output = subprocess.run(device_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True, timeout=20)
        private_ip_op = device_output.stdout
        private_ip_match = re.search(fr'{interface_name}\s+(\d+\.\d+\.\d+\.\d+)', private_ip_op)

        if private_ip_match:
            private_ip = private_ip_match.group(1)
            print(f"Private IP: {private_ip}")
            return private_ip
        else:
            print("Private IP  not found.")
            return ""

    except subprocess.CalledProcessError:
        print("Failed to execute Device IP command in find_gateway")
        return ""  
    except subprocess.TimeoutExpired:
        print("Device IP  command timed out from find_gateway")
        return ""

def find_gateway(device_ip, ssh_username, ssh_password, ssh_port, successful_ips, failed_ips):
    print(device_ip)

    try:
        device_cmd = [
            "sshpass", "-p", ssh_password,
            "ssh", "-o", "StrictHostKeyChecking=no", "-p", str(ssh_port),
            f"{ssh_username}@{device_ip}",
            f"show ip route static "
        ]
       
        device_output = subprocess.run(device_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True, timeout=20)
        gateway_ip_op = device_output.stdout

        gateway_ip_match = re.search(r'0.0.0.0/0 \[\d+/\d+\] via (\d+\.\d+\.\d+\.\d+)', gateway_ip_op)
        if gateway_ip_match:
            gateway_ip = gateway_ip_match.group(1)
            print(f"Gateway IP: {gateway_ip}")
            successful_ips.append(device_ip) 

            interface_name = check_interface_name(device_ip, ssh_username, ssh_password, ssh_port, gateway_ip)
            if interface_name != "":
                private_ip = get_ip_from_interface_name(device_ip, ssh_username, ssh_password, ssh_port, interface_name)
                print(private_ip)

        else:
            print("Gateway IP not found.")
            failed_ips.append(device_ip) 
            return ""

    except subprocess.CalledProcessError:
        print("Failed to execute Device IP command in find_gateway")
        gateway_ip = ""  
    except subprocess.TimeoutExpired:
        print("Device IP  command timed out from find_gateway")
        gateway_ip = ""






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

    device_sql = "SELECT device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, vendor, type, cust_id FROM fn_edge_devices WHERE vendor='Cisco'"
    cursor.execute(device_sql)
    result = cursor.fetchall()

    successful_ips = Manager().list()
    failed_ips = Manager().list()

    process_list = []

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
        process = multiprocessing.Process(target=find_gateway, args=(device_ip, ssh_username, ssh_password, ssh_port, successful_ips, failed_ips,))
        process_list.append(process)

    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    # Print the summary

    cursor.close()  
    conn.close()