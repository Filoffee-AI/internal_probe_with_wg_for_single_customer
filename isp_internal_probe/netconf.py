import yaml
import subprocess
import re
import socket
import time
import tempfile

def get_default_interface():
    try:
        output = subprocess.check_output("ip route show default", shell=True, text=True)
        match = re.search(r'default via .* dev (\S+)', output)
        return match.group(1) if match else None
    except subprocess.CalledProcessError:
        return None

def get_current_ip(interface):
    if not interface:
        return None
    try:
        output = subprocess.check_output(f"ip a show {interface}", shell=True, text=True)
        match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)/', output)
        return match.group(1) if match else None
    except subprocess.CalledProcessError:
        return None

def check_dns():
    try:
        socket.gethostbyname("google.com")
        return True
    except socket.gaierror:
        return False
    

def add_cron_jobs():
    """Clear existing crontab and add required cron jobs"""

    cron_jobs = [
        '*/15 * * * * cd /home/isp_internal_probe && python3 check_config_update_run_probe_initial.py >> /home/isp_internal_probe/logs/inital_logs_$(date +\%Y\%m\%d).log',
        '*/30 * * * * cd /home/isp_internal_probe && sudo sh probe_intial.sh >> /home/isp_internal_probe/logs/inital_logs_$(date +\%Y\%m\%d).log',
        '*/10 * * * * cd /home/isp_internal_probe && python3 test_ssh_snmp.py >> /home/isp_internal_probe/logs/test_ssh_snmp_$(date +\%Y\%m\%d).log',
        '*/30 * * * * cd /home/isp_internal_probe && sudo sh ssh_key_clear.sh',
        '0 */12 * * * cd /home/isp_internal_probe && python3 delete_old_logs.py',
        '* * * * * cd /home/isp_internal_probe && python3 get_octates.py >> /home/isp_internal_probe/logs/utilization_log_$(date +\%Y\%m\%d).log',
        '* * * * * cd /home/isp_internal_probe && python3 get_push_edge_device_ping_status.py >> /home/isp_internal_probe/logs/ed_ping_status_log_$(date +\%Y\%m\%d).log',
        '* * * * * cd /home/isp_internal_probe && python3 internal_probe_main_script.py >> /home/isp_internal_probe/logs/polling_logs_$(date +\%Y\%m\%d).log',
        '* * * * * cd /home/isp_internal_probe && python3 poll_non_meraki_dbb_links.py >> /home/isp_internal_probe/logs/dbb_non_polling_logs_$(date +\%Y\%m\%d).log',
        '* * * * * cd /home/isp_internal_probe && python3 poll_meraki_dbb_links.py >> /home/isp_internal_probe/logs/dbb_meraki_polling_logs_$(date +\%Y\%m\%d).log',
        '*/5 * * * * cd /home/isp_internal_probe && python3 check_isp_down_for_cisco.py >> /home/isp_internal_probe/logs/check_link_down_for_cisco_$(date +\%Y\%m\%d).log',
    ]

    subprocess.run("crontab -r", shell=True, stderr=subprocess.DEVNULL)  

    # Step 2: Create a temporary file with new crontab jobs
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_cron:
        temp_cron.write("\n".join(cron_jobs) + "\n")
        temp_filename = temp_cron.name
    
    
    # Step 3: Load the new crontab
    subprocess.run(f"crontab {temp_filename}", shell=True)

    print("Crontab cleared and new jobs added successfully.")
    
# Detect default network interface
interface = get_default_interface()
if not interface:
    print("No active network interface found. Exiting...")
    exit(1)

# Check existing IP configuration
current_ip = get_current_ip(interface)
dns_reachable = check_dns()

if current_ip and dns_reachable:
    print(f"Current IP: {current_ip} on {interface}")
    print("DNS is reachable. No need to configure the network.\n")
    print("Starting required services...!!!")
    subprocess.run(["systemctl", "start", "dc_script.service"])
    time.sleep(2)
    subprocess.run(["systemctl", "status", "dc_script.service"])
    
    add_cron_jobs()
    
else:
    print("=" * 50)
    print(" " * 20 + "NETWORK CONFIGURATION" + " " * 20)
    print("=" * 50)

    ip_type = input('Enter IP configuration type (static/dhcp): ').lower()

    if ip_type == 'static':
        ip_address = input('Enter IP address: ')
        netmask = input('Enter netmask in CIDR notation (e.g. 24): ')
        gateway = input('Enter gateway: ')
        dns_servers = input('Enter comma-separated DNS servers: ').split(',')

        print("=" * 50)
        print(" " * 20 + "NETWORK DETAILS" + " " * 20)
        print("=" * 50)
        print(f"Interface: {interface}")
        print(f"IP Address: {ip_address}")
        print(f"Netmask: {netmask}")
        print(f"Gateway: {gateway}")
        print(f"DNS Servers: {', '.join(dns_servers)}")

        # Define static IP configuration
        network_config = {
            'network': {
                'version': 2,
                'renderer': 'networkd',
                'ethernets': {
                    interface: {
                        'addresses': [ip_address+'/'+netmask],
                        'routes': [{'to': '0.0.0.0/0', 'via': gateway}],
                        'nameservers': {
                            'addresses': dns_servers
                        }
                    }
                }
            }
        }
    else:
        print("=" * 50)
        print(" " * 20 + "NETWORK DETAILS" + " " * 20)
        print("=" * 50)
        print(f"Using DHCP for network configuration on {interface}.")

        # Define DHCP configuration
        network_config = {
            'network': {
                'version': 2,
                'renderer': 'networkd',
                'ethernets': {
                    interface: {
                        'dhcp4': True,
                        'optional': True,
                    }
                }
            }
        }

    confirm = input("Do you want to apply this configuration (y/n)? ").lower()
    if confirm == "y":
        # Write configuration to netplan file
        with open('/etc/netplan/01-netcfg.yaml', 'w') as file:
            yaml.dump(network_config, file)

        # Apply configuration
        subprocess.run(['netplan', 'apply'])
        print("Network configuration applied. Checking connectivity...")

        # Re-check DNS after applying
        if check_dns():
            print("DNS is now reachable. Configuration successful!\n")
            
            print("Starting required services...!!!")
            subprocess.run(["systemctl", "start", "dc_script.service"])
            time.sleep(2)
            subprocess.run(["systemctl", "status", "dc_script.service"])
            
            add_cron_jobs()
            
            
        else:
            print("Warning: DNS is still not reachable. Please check manually.")
