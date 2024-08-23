import subprocess
import socket
import ssl
from config_class import config

wg_conf = config.wg_conf
wg_server = wg_conf['wg_server']
wg_username = wg_conf['wg_username']
wg_password = wg_conf['wg_password']
wg_link = wg_conf['wg_link']
wg_subnet = wg_conf['wg_subnet']
wg_connection = wg_conf['wg_connection']
wg_http_port = wg_conf['wg_http_port']
wg_udp_port = wg_conf['wg_udp_port']

print("Performing Health Checks...")
# DNS resolution
try:
    socket.gethostbyname(f'{wg_connection}')
    print(f'DNS resolution for {wg_connection} successful')
except socket.gaierror:
    print(f'DNS resolution for {wg_connection} failed')
    exit(1)

# HTTPS reachability
try:
    context = ssl.create_default_context()
    with socket.create_connection((wg_connection, wg_http_port)) as sock:
        with context.wrap_socket(sock, server_hostname=wg_connection) as ssock:
            ssock.sendall(b'GET / HTTP/1.1\r\nHost: linkeye.io\r\n\r\n')
            response = ssock.recv(1024)
            if response:
                print(f'{wg_connection} is reachable on HTTPS')
            else:
                print(f'{wg_connection} is not reachable on HTTPS')
                exit(1)
except:
    print(f'Error connecting to {wg_connection} on HTTPS')
    exit(1)

# UDP reachability
try:
    subprocess.run(['sudo', 'nc', '-vz', '-u', f'{wg_link}', f'{wg_udp_port}'], check=True)
    print(f'{wg_link} is reachable on UDP port {wg_udp_port}')
except subprocess.CalledProcessError:
    print(f'{wg_link} is not reachable on UDP port {wg_udp_port}')
    exit(1)

# If all tests pass, run wireguard-start.py
# subprocess.run(['sudo', 'python3', '/home/isp_internal_probe/wireguard-start.py'], check=True)
subprocess.run("python3 wireguard-start.py", shell=True, cwd="/home/isp_internal_probe", check=True)
ping_command = f"ping -c 1 {wg_server}"
ping_process = subprocess.run(ping_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if ping_process.returncode == 0:
    print("WireGuard Setup Successful")
    # subprocess.run(['sudo', 'python3', '/home/isp_internal_probe/register_probe.py'], check=True)
    subprocess.run("python3 register_probe.py", shell=True, cwd="/home/isp_internal_probe", check=True)
    print("Local Proe Installtion Successful...Restarting the Server")
    subprocess.run(['sudo', 'reboot'], check=True)
else:
    # 10.75.0.1 is reachable, print error message
    print("WireGuard Setup Failed")
