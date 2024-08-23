import json
import paramiko
import sys
import time
import mysql.connector
from config_class import config

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

def check_wan_status(vendor_id, isp_wan_id, device_id):
    main_dict = {'wan_code': -1}

    try:
        conn = mysql.connector.connect(
		user=config.mysql_conf["user"],
		password=config.mysql_conf["password"],
        host=config.mysql_conf["host"],
    	database=config.mysql_conf["database"],
    	auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()

        cursor.execute("""SELECT internal_ip from fn_isp_details WHERE isp_wan_id = '{}';""".format(isp_wan_id))
        result = cursor.fetchone()

        if result is None:
           return 0
                  
        wan_ip = result[0]

        cursor.execute("""SELECT device_ip, ssh_username, ssh_password, ssh_port, type from fn_edge_devices WHERE device_id = '{}';""".format(device_id))
        ed_result = cursor.fetchone()

        if ed_result is None:
           return 0
        
        device_ip = ed_result[0]          
        ssh_username = ed_result[1]
        ssh_password = ed_result[2]
        ssh_port = ed_result[3]
        type = ed_result[4]


        if vendor_id == 2: 
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=4)

            channel = ssh.invoke_shell()
            time.sleep(1)  
            channel.send('a\n')

            wan_dict = {}
            commands = [f"execute ping-options source {wan_ip}", f"execute ping {wan_ip}"]
            output = ""
            for cmd in commands:
                channel.send(cmd + "\n")
                time.sleep(2)  

                while channel.recv_ready():
                    output += channel.recv(1024).decode()
                    time.sleep(1)  

            for line in output.splitlines():
                if 'packet loss' in line:
                    packet_loss = line.split(' ')[-3][:-1]
                    wan_dict["packet_loss"] = int(packet_loss)
                    if wan_dict["packet_loss"] == 100:
                        main_dict['wan_code'] = -1
                    else:
                        main_dict['wan_code'] = 1

                if 'round-trip' in line:
                    rtt = line.split('/')[-2]
                    wan_dict["latency"] = rtt
                    main_dict['wan_code'] = 1

            main_dict["wan"] = wan_dict
        elif vendor_id == 13:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=5)

            channel = ssh.invoke_shell()
            time.sleep(1)  
            channel.send('a\n')

            wan_dict = {}
            commands = [f"ping {wan_ip} source {wan_ip} count 4"]
            output = ""
            for cmd in commands:
                channel.send(cmd + "\n")
                time.sleep(2)  

                while channel.recv_ready():
                    output += channel.recv(1024).decode()
                    time.sleep(1)  

            for line in output.splitlines():
                if 'packet loss' in line:
                    packet_loss = line.split(', ')[2].split('%')[0]
                    wan_dict["packet_loss"] = int(packet_loss)
                    if wan_dict["packet_loss"] == 100:
                        main_dict['wan_code'] = -1
                    else:
                        main_dict['wan_code'] = 1

                if 'rtt min/avg/max/mdev =' in line:
                    rtt = line.split('/')[4]
                    wan_dict["latency"] = rtt
                    main_dict['wan_code'] = 1

            main_dict["wan"] = wan_dict
        elif vendor_id == 12:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.load_system_host_keys()
            ssh.connect(hostname=device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=5)
            time.sleep(5)

            channel = ssh.invoke_shell()
            time.sleep(1)  

            wan_dict = {}
            commands = [f"ping {wan_ip} -I {wan_ip} -c 4"]
            time.sleep(3)
            
            output = ""

            for cmd in commands:
                channel.send(cmd + "\n")
                time.sleep(2)  

                while channel.recv_ready():
                    output += channel.recv(1024).decode()
                    time.sleep(1)  

            for line in output.splitlines():
                if 'packet loss' in line:
                    packet_loss = line.split(', ')[2].split('%')[0]
                    wan_dict["packet_loss"] = int(packet_loss)
                    if wan_dict["packet_loss"] == 100:
                        main_dict['wan_code'] = -1
                    else:
                        main_dict['wan_code'] = 1

                if 'rtt min/avg/max/mdev =' in line:
                    rtt = line.split('/')[4]
                    wan_dict["latency"] = rtt
                    main_dict['wan_code'] = 1

            main_dict["wan"] = wan_dict
        elif vendor_id == 6: 
            if type == "Router":
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=4)

                channel = ssh.invoke_shell()
                time.sleep(1)  

                wan_dict = {}
                commands = [f"ping {wan_ip} source {wan_ip}"]
                output = ""
                for cmd in commands:
                    channel.send(cmd + "\n")
                    time.sleep(2)  

                    while channel.recv_ready():
                        output += channel.recv(1024).decode()
                        time.sleep(1)  

                for line in output.splitlines():
                    if 'Success rate is' in line:
                        packet_loss = 100 - int(line.split(' ')[3])
                        wan_dict["packet_loss"] = int(packet_loss)
                        if wan_dict["packet_loss"] == 100:
                            main_dict['wan_code'] = -1
                        else:
                            main_dict['wan_code'] = 1

                    if 'round-trip min/avg/max' in line:
                        fields = line.split('=')[-1].split('/')
                        avg_latency = int(fields[1])
                        wan_dict["latency"] = avg_latency

                main_dict["wan"] = wan_dict
        elif vendor_id == 14:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=device_ip, port=ssh_port, username=ssh_username, password=ssh_password, allow_agent=False, look_for_keys=False, timeout=5)

            channel = ssh.invoke_shell()
            time.sleep(2)  

            wan_dict = {}
            commands = [f"ping source {wan_ip} count 4 host {wan_ip}"]
            output = ""
            for cmd in commands:
                channel.send(cmd + "\n")
                time.sleep(4)  

                while channel.recv_ready():
                    output += channel.recv(1024).decode()
                    time.sleep(4)  

            for line in output.splitlines():
                if 'packet loss' in line:
                    packet_loss = line.split(', ')[2].split('%')[0]
                    wan_dict["packet_loss"] = int(packet_loss)
                    if wan_dict["packet_loss"] == 100:
                        main_dict['wan_code'] = -1
                    else:
                        main_dict['wan_code'] = 1

                if 'rtt min/avg/max/mdev =' in line:
                    rtt = line.split('/')[4]
                    wan_dict["latency"] = rtt
                    main_dict['wan_code'] = 1

            main_dict["wan"] = wan_dict
        else:
            vendor_id = "Not Implemented"

    except Exception as e:
        print(f"Error occurred: {e}")
        main_dict['wan_code'] = -1
        main_dict["wan"] = {"packet_loss": 100, "latency": "0"}

    finally:
        ssh.close()

    print(json.dumps(main_dict))

if __name__ == "__main__":

    vendor_id = int(sys.argv[1])
    isp_wan_id = int(sys.argv[2])
    device_id = int(sys.argv[3])

    check_wan_status(vendor_id, isp_wan_id, device_id)
