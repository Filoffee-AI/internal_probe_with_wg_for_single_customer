import subprocess
import paramiko
import mysql.connector
import json
import sys
from config_class import config
from pysnmp.hlapi import *
import nmap

device_id = sys.argv[1]
device_ip = sys.argv[2]


def is_ssh_port_open(host, ssh_port):
    nm = nmap.PortScanner()
    
    try:
        nm.scan(hosts=host, ports=f'{ssh_port}', arguments='-sT')
        tcp_state = nm[host].tcp(ssh_port)['state']
        tcp_result = 1 if 'open' in tcp_state else 0
        return tcp_result

    except KeyError as e:
        # This error typically occurs if the scanned port does not exist in the scan results
        return 0
    except Exception as e:
        return 0

def is_snmp_port_open(host, snmp_port):
    nm = nmap.PortScanner()
    
    try:
        nm.scan(hosts=host, ports=f'{snmp_port}', arguments='-sU')
        udp_state = nm[host]['udp'][snmp_port]['state'] if 'udp' in nm[host] and snmp_port in nm[host]['udp'] else 'not scanned'
        udp_result = 1 if 'open' in udp_state else 0
        
        return udp_result

    except KeyError as e:
        # This error typically occurs if the scanned port does not exist in the scan results
        return 0
    except Exception as e:
        return 0


def test_snmp_credentials(data):
    ip, snmp_str, version, security_level, auth_type, auth_password, privacy_type, privacy_password = data[0], data[4], data[5], data[6], data[7], data[8], data[9], data[10]
    snmp_port_status = is_snmp_port_open(ip, 161)

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
        return {'snmp_port_status': 1, 'snmp_auth_status': 0}
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'snmp_port_status': 1, 'snmp_auth_status': 1}
    except subprocess.CalledProcessError:
        return {'snmp_port_status': 1, 'snmp_auth_status': 0}


def test_ssh_credentials(data):
    ip, username, password, port = data[0], data[1], data[2], int(data[3])
    ssh_port_status = is_ssh_port_open(ip, port)

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


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host=config.mysql_conf["host"],
        user=config.mysql_conf["user"],
        password=config.mysql_conf["password"],
        database=config.mysql_conf["database"]
    )
    
    cursor = mydb.cursor()
    cursor.execute("SELECT device_ip, ssh_username, ssh_password, ssh_port, snmp_str, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password FROM fn_edge_devices where device_id=%s and device_ip=%s", (device_id, device_ip))
    data = cursor.fetchone()
    mydb.close()

    response = {}
    if data is not None:
        snmp_results = test_snmp_credentials(data)
        ssh_results = test_ssh_credentials(data)
        response = {
            'code': 1,
            'message': 'successfully extracted',
            'ssh_port_status': ssh_results['ssh_port_status'],
            'ssh_auth_status': ssh_results['ssh_auth_status'],
            'snmp_port_status': snmp_results['snmp_port_status'],
            'snmp_auth_status': snmp_results['snmp_auth_status']
        }
    else:
        response = {'code': -1, 'message': "device not found"}
        
    print(json.dumps(response))
