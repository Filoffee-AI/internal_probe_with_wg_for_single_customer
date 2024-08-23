import paramiko
import re
from paramiko.ssh_exception import AuthenticationException, SSHException
import mysql.connector
import subprocess
from config_class import config
import datetime
import multiprocessing
from multiprocessing import Manager
import subprocess

def execute_ssh_command(device_ip, ssh_username, ssh_password, command, ssh_port=22):
    try:
        # Set up Paramiko SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Establish SSH connection
        ssh.connect(device_ip, port=ssh_port, username=ssh_username, password=ssh_password, timeout=15)
        stdin, stdout, stderr = ssh.exec_command(command)
        command_output = stdout.read().decode('utf-8')
        ssh.close()
        
        return command_output

    except AuthenticationException:
        print(f"Authentication failed for {device_ip}")
    except SSHException as e:
        print(f"SSH error for {device_ip}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {device_ip}: {e}")
    finally:
        ssh.close()  # Ensure the connection is closed even in case of exceptions


def snmpwalk_for_cisco_router(device_ip, snmp_str, interface_name):
    command = ['snmpwalk', '-v', '2c', '-c', snmp_str, device_ip, "IF-MIB::ifDescr"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        snmp_data = result.stdout
        for line in snmp_data.splitlines():
            match = re.search(r"IF-MIB::ifDescr\.(\d+) = STRING: (.+)$", line)
            if match:
                if_name = match.group(2)
                if_index = int(match.group(1))
                if if_name.strip() == interface_name.strip():
                    ifname_command = ['snmpwalk', '-v', '2c', '-c', snmp_str, device_ip, "ifName", f"| grep 'ifName.{if_index}\b'"]
                    ifname_res = subprocess.run(ifname_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    ifname_data = ifname_res.stdout
                    for line in ifname_data.splitlines():
                        match = re.search(r"ifName\.(\d+) = STRING: (.+)$", line)
                        if match:
                            if_name = match.group(2)
                            if_index_ifname = int(match.group(1))
                            if if_index == if_index_ifname:
                                return if_index, if_name
    else:
        return None, None
    
def update_bb_for_cisco_router_in_table(conn, cursor, ip_address, if_index, if_name, location_id, device_id, device_ip, cust_id):
    try:
        check_ip_qry = f"SELECT isp_wan_id from fn_isp_details WHERE public_ip='{ip_address}' AND link_type='DBB' AND location_id='{location_id}'"
        cursor.execute(check_ip_qry)
        result = cursor.fetchall()
        if len(result) == 0:
            qry = f"""INSERT INTO `fn_isp_details` (`isp_wan_id`, `edge_device_id`, `cust_id`, `location_id`, `public_ip`, `private_ip`, `internal_ip`, `vendor_id`, `default_gateway`, `firewall_ip`, `link_type`, `if_name`, `if_index`) 
                                VALUES ('-1', '{device_id}', '{cust_id}', '{location_id}', '{ip_address}', 'None', '{ip_address}', '-1', '0.0.0.0', '{device_ip}', 'DBB', '{if_name}', '{if_index}')"""
        else:
            isp_wan_id = result[0][0]
            qry = f"UPDATE `fn_isp_details` SET `if_name`='{if_name}', `if_index`='{if_index}', `edge_device_id`='{device_id}', `firewall_ip`='{device_ip}' WHERE  `isp_wan_id`='{isp_wan_id}'"
        cursor.execute(qry)
        conn.commit()
        print("Database update successful.")
    except Exception as e:
        print(f"An error occurred while updating the database: {e}")
        conn.rollback()


def find_bb_link_for_cisco_router(device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, vendor, type, cust_id, successful_ips, failed_ips):
    conn = mysql.connector.connect(
        host=config.mysql_conf["host"],
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        port=config.mysql_conf["port"],
        database=config.mysql_conf["database"],
        auth_plugin=config.mysql_conf["auth_plugin"]
    )
    cursor = conn.cursor()
    try:
        # Execute the command
        command_output = execute_ssh_command(device_ip, ssh_username, ssh_password, "show ip route static", ssh_port)
        
        if 'S*' in command_output:
            # Parse the command output to find IPs
            ip_list = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', command_output)
            filtered_ips = []
            for ip in ip_list:
                if ip != '0.0.0.0' and ip not in filtered_ips:
                    filtered_ips.append(ip)
            print(f"Filtered IPs: {filtered_ips}")

            # find interface name for ip address
            interface_names = []
            for ip in filtered_ips:
                shorten_ip = '.'.join(ip.split('.')[:3])
                interface_name_output = execute_ssh_command(device_ip, ssh_username, ssh_password, f"show ip route connected | include {shorten_ip}", ssh_port)
                relevant_lines = [line.strip() for line in interface_name_output.splitlines() if shorten_ip in line]
                for line in relevant_lines:
                    match = re.search(rf'\b[C]\s+{shorten_ip}\.\d+/\d+\s+is\s+directly\s+connected,\s+([\w/]+)', line)
                    if match:
                        interface_names.append(match.group(1))

            print(f"Interface Names: {interface_names}")

            # find ip addresses
            for interface_name in interface_names:
                bb_ip_command_output = execute_ssh_command(device_ip, ssh_username, ssh_password, f"show ip int brief {interface_name}", ssh_port)
                ip_address_match = re.search(rf"{interface_name}\s+([\d.]+)\s+\w+\s+\w+\s+(\w+)\s+(\w+)", bb_ip_command_output)
                if ip_address_match:
                    ip_address = ip_address_match.group(1)
                    status = ip_address_match.group(3)
                    if status.lower() == "up":
                        check_ip_qry = f"SELECT * from fn_isp_details WHERE public_ip='{ip_address}' AND link_type='ILL'"
                        cursor.execute(check_ip_qry)
                        result = cursor.fetchall()

                        if len(result) == 0:
                            if_index = None
                            if_index, if_name = snmpwalk_for_cisco_router(device_ip, snmp_str, interface_name)

                            print(f"ifindex {if_index} for interface_name {if_name} for ip_address {ip_address}")
                            update_bb_for_cisco_router_in_table(conn, cursor, ip_address, if_index, if_name, location_id, device_id, device_ip, cust_id)
                else:
                    print(f"No IP address found for interface {interface_name}")

            successful_ips.extend(device_ip)
        else:
            print(f"No 'S*' routes found in the output for {device_ip}")
        
    except AuthenticationException:
        print(f"Authentication failed for {device_ip}")
        failed_ips.append(device_ip)
    except SSHException as e:
        print(f"SSH error for {device_ip}: {e}")
        failed_ips.append(device_ip)
    except Exception as e:
        print(f"An error occurred while processing {device_ip}: {e}")
        failed_ips.append(device_ip)
    finally:
        cursor.close()  
        conn.close()


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
    print(f"Info: SNMP Walk Started at:{start_time}")
    
    successful_ips = Manager().list()
    failed_ips = Manager().list()

    process_list = []

    device_sql = "SELECT device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, vendor, type, cust_id FROM fn_edge_devices where vendor='Cisco'"
    cursor.execute(device_sql)
    result = cursor.fetchall()
    

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
        process = multiprocessing.Process(target=find_bb_link_for_cisco_router, args=(device_id, device_ip, location_id, snmp_str, ssh_username, ssh_password, ssh_port, vendor, type, cust_id, successful_ips, failed_ips,))
        process_list.append(process)

    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    cursor.close()  
    conn.close()


    total_ips = len(successful_ips) + len(failed_ips)
    now = datetime.datetime.now()
    end_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"Info: SNMP Walk Completed at:{end_time}")
