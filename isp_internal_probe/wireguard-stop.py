import subprocess
from config_class import config


wg_conf = config.wg_conf
wg_server = wg_conf['wg_server']
wg_username = wg_conf['wg_username']
wg_password = wg_conf['wg_password']
wg_link = wg_conf['wg_link']
wg_subnet = wg_conf['wg_subnet']
# Fetch the content of /etc/wireguard/public.key
with open('/etc/wireguard/public.key', 'r') as f:
    public_key = f.read().strip()

# Run the SSH command to remove the peer
remove_peer = f'sshpass -p "{wg_password}" ssh -o StrictHostKeyChecking=no {wg_username}@{wg_link} sudo wg set wg0 peer {public_key} remove'
subprocess.run(remove_peer, shell=True, check=True)
disable_wireguard = f'sudo systemctl disable wg-quick@wg0.service'
subprocess.run(disable_wireguard, shell=True, check=True)
stop_wireguard = f'sudo systemctl stop wg-quick@wg0.service'
subprocess.run(stop_wireguard, shell=True, check=True)
default_wg = f'sudo cp /etc/wireguard/wg0-default.conf /etc/wireguard/wg0.conf'
subprocess.run(default_wg, shell=True, check=True)
