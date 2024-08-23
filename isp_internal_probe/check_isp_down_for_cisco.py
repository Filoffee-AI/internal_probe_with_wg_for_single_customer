import mysql.connector
import subprocess
import re
import multiprocessing
from multiprocessing import Pool

def check_ip_got_changed(args):
    isp_wan_id, internal_ip, if_name, if_index, device_ip, snmp_str, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password = args
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='GyanFilo@2023',
            database='filo_nms'
        )
        cursor = conn.cursor()
        
        if snmp_version == 2:
            snmp_cmd = ['snmpwalk', '-v2c', '-c', snmp_str, device_ip, 'RFC1213-MIB::ipAdEntIfIndex']
        elif snmp_version == 3:
            if security_level == "0":
                snmp_cmd = ['snmpwalk', '-v3', '-u', snmp_str, device_ip, 'RFC1213-MIB::ipAdEntIfIndex']
            elif security_level == "1":
                snmp_cmd = ['snmpwalk', '-v3', '-l', 'authNoPriv', '-u', snmp_str, '-a', auth_type, '-A', auth_password, device_ip, 'RFC1213-MIB::ipAdEntIfIndex']
            elif security_level == "2":
                snmp_cmd = ['snmpwalk', '-v3', '-l', 'authPriv', '-u', snmp_str, '-a', auth_type, '-A', auth_password, '-x', privacy_type, '-X', privacy_password, device_ip, 'RFC1213-MIB::ipAdEntIfIndex']

        ifname_output = subprocess.run(snmp_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if ifname_output.returncode != 0:
            print(f"Error executing SNMP command for device {device_ip}: {ifname_output.stderr.decode('utf-8')}")
            return

        ifname_output_lines = ifname_output.stdout.decode('utf-8').split('\n')

        matched_line = None
        for line in ifname_output_lines:
            match = re.match(r'RFC1213-MIB::ipAdEntIfIndex\.(\d+\.\d+\.\d+\.\d+) = INTEGER: (\d+)', line)
            if match:
                ip = match.group(1)
                index = match.group(2)
                if ip == internal_ip and index == if_index:
                    matched_line = line
                    break

        if matched_line:
            print(f"Matched line: {matched_line}")
        else:
            for line in ifname_output_lines:
                match = re.match(r'RFC1213-MIB::ipAdEntIfIndex\.(\d+\.\d+\.\d+\.\d+) = INTEGER: (\d+)', line)
                if match:
                    ip = match.group(1)
                    index = match.group(2)
                    if index == if_index:
                        cursor.execute("UPDATE fn_isp_details SET internal_ip=%s WHERE isp_wan_id=%s", (ip, isp_wan_id))
                        conn.commit()
                        print(f"Updating with new IP: {ip} for index: {if_index}")
                        break

        cursor.close()
        conn.close()
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error for device {device_ip}: {e}")
    except mysql.connector.Error as err:
        print(f"Database error for device {device_ip}: {err}")
    except Exception as e:
        print(f"Unexpected error for device {device_ip}: {e}")

def main():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='GyanFilo@2023',
            database='filo_nms'
        )
        cursor = conn.cursor()
        cursor.execute("""SELECT fn_isp_details.isp_wan_id, fn_isp_details.internal_ip, fn_isp_details.if_name, fn_isp_details.if_index, fn_edge_devices.device_ip, fn_edge_devices.snmp_str, fn_edge_devices.snmp_version, fn_edge_devices.security_level, fn_edge_devices.auth_type, fn_edge_devices.auth_password, fn_edge_devices.privacy_type, fn_edge_devices.privacy_password 
                          FROM fn_edge_devices, fn_isp_details 
                          WHERE fn_edge_devices.device_id=fn_isp_details.edge_device_id AND fn_edge_devices.vendor='Cisco' AND fn_edge_devices.type='Router'""")
        result = cursor.fetchall()
        
        # Use multiprocessing Pool to parallelize the task
        pool = Pool(processes=multiprocessing.cpu_count())
        pool.map(check_ip_got_changed, result)

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
