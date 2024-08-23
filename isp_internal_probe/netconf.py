import yaml
import subprocess

# Print the banner
print("=" * 50)
print(" " * 20 + "NETWORK CONFIGURATION" + " " * 20)
print("=" * 50)

# Prompt the user for network configuration details
ip_type = input('Enter IP configuration type (static/dhcp): ').lower()

if ip_type == 'static':
    ip_address = input('Enter IP address: ')
    netmask = input('Enter netmask in CIDR notation (e.g. 24): ')
    gateway = input('Enter gateway: ')
    dns_servers = input('Enter comma-separated DNS servers: ').split(',')

    # Print the network details
    print("=" * 50)
    print(" " * 20 + "NETWORK DETAILS" + " " * 20)
    print("=" * 50)
    print(f"IP Address: {ip_address}")
    print(f"Netmask: {netmask}")
    print(f"Gateway: {gateway}")
    print(f"DNS Servers: {', '.join(dns_servers)}")

    # Define the network configuration for static IP
    network_config = {
        'network': {
            'version': 2,
            'renderer': 'networkd',
            'ethernets': {
                'ens160': {
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
    # Print the network details
    print("=" * 50)
    print(" " * 20 + "NETWORK DETAILS" + " " * 20)
    print("=" * 50)
    print("Using DHCP for network configuration.")

    # Define the network configuration for DHCP
    network_config = {
        'network': {
            'version': 2,
            'renderer': 'networkd',
            'ethernets': {
                'ens160': {
                    'dhcp4': True,
                    'optional': True,
                }
            }
        }
    }

# Confirm with the user before applying the configuration
confirm = input("Do you want to apply this configuration (y/n)? ").lower()

if confirm == "y":
    # Write the configuration to a YAML file
    with open('/etc/netplan/01-netcfg.yaml', 'w') as file:
        yaml.dump(network_config, file)

    # Apply the configuration using netplan apply command
    subprocess.run(['netplan', 'apply'])

    # Print the completion message
    print("Network configuration completed.")
    print("Configuring Services...Please wait...")
