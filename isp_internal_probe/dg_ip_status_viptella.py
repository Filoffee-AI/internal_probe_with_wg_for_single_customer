import json
import os
import sys

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
port = sys.argv[4]
wan_ip = sys.argv[5]
dg_ip = sys.argv[6]

main_dict = {}

try:

    output = os.popen(f'''sshpass -p {password} ssh -o StrictHostKeyChecking=no -p {port} {username}@{host} -T << EOF 
    ping {dg_ip} source-ip {wan_ip}''').read()

    # output = os.popen(f'''sshpass -p {password} ssh -o StrictHostKeyChecking=no -p {port} {username}@{host} "execute ping {dg_ip}"''').read()
    dg_dict = {}
    status = -2
    for line in output.splitlines():
        if 'packet loss' in line:
            packet_loss = line.split(' ')[-3][:-1]
            dg_dict["packet_loss"] = int(packet_loss)
            if dg_dict["packet_loss"] == 100:
                main_dict['dg_message'] = "Gateway Not Reachable"
                main_dict['dg_code'] = -1
                status = -1
            else:
                main_dict['dg_message'] = "Gateway Reachable"
                main_dict['dg_code'] = 1
                status = 1
        if 'round-trip' in line:
            rtt = line.split('/')[-2]
            dg_dict["latency"] = rtt
            main_dict['dg_message'] = "Gateway Reachable"
            main_dict['dg_code'] = 1
            
    if status == -2:
        main_dict['dg_message'] = "Invalid Credentials"
        main_dict['dg_code'] = -1

except:
    main_dict['dg_message'] = "Gateway Not Reachable"
    main_dict['dg_code'] = -1


    dg_dict["packet_loss"] = 100
    dg_dict["latency"] = 0
    # print("Unable to connect")

main_dict["dg"] = dg_dict

print(json.dumps(main_dict))
