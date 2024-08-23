import json
import os
import sys
import subprocess
import paramiko
import time


host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
port = sys.argv[4]
wan_ip = sys.argv[5]
dg_ip = sys.argv[6]
dg_dict = {}
main_dict = {}

commands = [f"execute ping-options source {wan_ip}", f"execute ping {dg_ip}"]

# Create an SSH client and set StrictHostKeyChecking to 'no'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password, allow_agent=False, look_for_keys=False, timeout=4)

try:
    # Handle the "(Press 'a' to accept)" prompt
    channel = ssh.invoke_shell()
    time.sleep(1)  # Wait for the initial prompt to appear
    channel.send('a\n')

    # Execute the commands and collect their output
    output = ""
    
    sleep_time = 1
    for cmd in commands:
        channel.send(cmd + "\n")
        time.sleep(sleep_time)  # Wait for the command to execute
        while channel.recv_ready():
            output += channel.recv(1024).decode()
        sleep_time = 6

    if "packet loss" not in output:
        raise Exception("SSH command executed, but the output is empty")

    # Print or process the collected output
    # print("Command output:")
    # print(output)
    for line in output.splitlines():
        if 'packet loss' in line:
            packet_loss = line.split(' ')[-3][:-1]
            dg_dict["packet_loss"] = int(packet_loss)
            if dg_dict["packet_loss"] == 100:
                main_dict['dg_message'] = "Gateway Not Reachable"
                main_dict['dg_code'] = -1
            else:
                main_dict['dg_message'] = "Gateway Reachable"
                main_dict['dg_code'] = 1
        if 'round-trip' in line:
            rtt = line.split('/')[-2]
            dg_dict["latency"] = rtt
            main_dict['dg_message'] = "Gateway Reachable"
            main_dict['dg_code'] = 1
except Exception as ex:
    # print(f"An error occurred: {str(ex)}")
    main_dict['dg_message'] = "Gateway Not Reachable"
    main_dict['dg_code'] = -1

    dg_dict["packet_loss"] = 100
    dg_dict["latency"] = 0
finally:
    ssh.close()

main_dict["dg"] = dg_dict

print(json.dumps(main_dict))
