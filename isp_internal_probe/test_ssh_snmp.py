import subprocess
import paramiko
import mysql.connector
import concurrent.futures
import json
import requests
import datetime
from config_class import config
import nmap

   
def check_snmp_port_status(host, snmp_port):
    nm = nmap.PortScanner()
    
    try:
        nm.scan(hosts=host, ports=f'{snmp_port}', arguments='-sU')
        udp_state = nm[host]['udp'][snmp_port]['state'] if 'udp' in nm[host] and snmp_port in nm[host]['udp'] else 'not scanned'
        udp_result = 1 if 'open' in udp_state else 0
        
        return udp_result

    except KeyError as e:
        # This error typically occurs if the scanned port does not exist in the scan results
        print(f"KeyError - make sure the port states are available: {e}")
        return 0
    except Exception as e:
        print(f"Scan failed: {e}")
        return 0


def check_ssh_port_status(host, ssh_port):
    nm = nmap.PortScanner()
    
    try:
        nm.scan(hosts=host, ports=f'{ssh_port}', arguments='-sT')
        tcp_state = nm[host].tcp(ssh_port)['state']
        tcp_result = 1 if 'open' in tcp_state else 0
        return tcp_result

    except KeyError as e:
        # This error typically occurs if the scanned port does not exist in the scan results
        print(f"KeyError - make sure the port states are available: {e}")
        return 0
    except Exception as e:
        print(f"Scan failed: {e}")
        return 0


def test_snmp_credentials(data):
    ip, snmp_str, version, security_level, auth_type, auth_password, privacy_type, privacy_password = data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]
    snmp_port_status = check_snmp_port_status(ip, 161)

    if snmp_port_status == 0:
        return {'snmp_port_status': 0, 'snmp_auth_status': 0}

    cmd = []  # Initialize cmd to an empty list

    if version == 2:
        cmd = ['snmpget', '-v2c', '-c', snmp_str, ip, '1.3.6.1.2.1.1.1.0']
    elif version == 3:
        if security_level == "0":
            cmd = ['snmpget', '-v3', '-u', snmp_str, ip, '1.3.6.1.2.1.1.1.0']
        elif security_level == "1":
            cmd = ['snmpget', '-v3', '-l', 'authNoPriv', '-u', snmp_str, '-a', auth_type, '-A', auth_password, ip, '1.3.6.1.2.1.1.1.0']
        elif security_level == "2":
            cmd = ['snmpget', '-v3', '-l', 'authPriv', '-u', snmp_str, '-a', auth_type, '-A', auth_password, '-x', privacy_type, '-X', privacy_password, ip, '1.3.6.1.2.1.1.1.0']
    else:
        print(f"Unsupported SNMP version: {version}")
        return {'snmp_port_status': 1, 'snmp_auth_status': 0}
    
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'snmp_port_status': 1, 'snmp_auth_status': 1}
    except subprocess.CalledProcessError:
        return {'snmp_port_status': 1, 'snmp_auth_status': 0}


def test_ssh_credentials(data):
    ip, username, password, port = data[3], data[11], data[12], int(data[13])
    ssh_port_status = check_ssh_port_status(ip, port)

    if ssh_port_status == 0:
        return {'ssh_port_status': ssh_port_status, 'ssh_auth_status': 0}

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=username, password=password, timeout=10)
        client.close()
        return {'ssh_port_status': 1, 'ssh_auth_status': 1}
    except Exception:
        return {'ssh_port_status': 1, 'ssh_auth_status': 0}


def test_device_credentials(data):
    snmp_results = test_snmp_credentials(data)
    ssh_results = test_ssh_credentials(data)
    current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = {
        "creds": {
            "username": config.creds['username'],
            "password": config.creds['password']
        },
        'device_id': data[0],
        'cust_id': data[2],
        'location_id': data[1],
        **snmp_results,
        **ssh_results,
        "time_stamp": current_timestamp
    }
    url = config.server + "api/push_snmp_ssh_status_of_edge_device.php"
    headers = {'Content-Type': 'application/json'}
    # print(payload)
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
        print(data[3], response.json())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host=config.mysql_conf["host"],
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        database=config.mysql_conf["database"]
    )
    
    cursor = mydb.cursor()
    sql = f""" SELECT device_id, location_id, cust_id, device_ip, snmp_str, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, ssh_username, ssh_password, ssh_port FROM fn_edge_devices"""
    cursor.execute(sql)
    credentials = cursor.fetchall()
    mydb.close()
    
    print("Testing in progress... Please wait.")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(test_device_credentials, credentials))

    # Convert the results into JSON format
    # print(json.dumps(results, indent=4))
    # api_response = post_to_api(results)
    # print(api_response)
