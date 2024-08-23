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
    output = os.popen(f'''sshpass -p {password} ssh -o StrictHostKeyChecking=no -p {port} {username}@{host} "execute ping {wan_ip}"''').read()
    wan_dict = {}
    for line in output.splitlines():
        if 'packet loss' in line:
            packet_loss = line.split(' ')[-3][:-1]
            wan_dict["packet_loss"] = int(packet_loss)
            if wan_dict["packet_loss"] == 100:
                main_dict['wan_message'] = "WAN IP Not Reachable"
                main_dict['wan_code'] = -1
            else:
                main_dict['wan_message'] = "WAN IP Reachable"
                main_dict['wan_code'] = 1
        
        if 'round-trip' in line:
            rtt = line.split('/')[-2]
            wan_dict["latency"] = rtt
            main_dict['wan_message'] = "WAN IP Reachable"
            main_dict['wan_code'] = 1
        
except:
    main_dict['wan_message'] = "WAN IP Not Reachable"
    main_dict['wan_code'] = -1


    wan_dict["packet_loss"] = packet_loss
    wan_dict["latency"] = 0


main_dict["wan"] = wan_dict

print(json.dumps(main_dict))