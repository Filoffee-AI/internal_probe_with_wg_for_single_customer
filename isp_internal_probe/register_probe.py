import subprocess

import requests
import os
import urllib3
import json
from cryptography.fernet import Fernet
from config_class import config


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print('Registering Probe .....')
customer_id = ""

json_file_path = '/home/isp_internal_probe/config.json'
field_to_check = 'client_id'

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        if field_to_check in data:
            field_value = data[field_to_check]
            if field_value == "AIR_001" or not field_value:
                # Field exists but is empty, so update it with the new value by Getting client_id
                customer_id = input('Enter your customer ID: ')
                data[field_to_check] = customer_id
                print(f"{field_to_check} field was empty and has been updated with value: {customer_id}")
            else:
                customer_id = field_value
        else:
            # Field doesn't exist, you can add it with the new value
            customer_id = input('Enter your customer ID: ')
            data[field_to_check] = customer_id
            print(f"{field_to_check} field didn't exist, so it was added with value: {customer_id}")

            with open(json_file_path, 'w') as new_json_file:
                json.dump(data, new_json_file, indent=4)

        # Send API request
        api_url = data['server'] + 'api/create_internal_probe.php'
        api_user = data['creds']['username']
        api_password = data['creds']['password']
else:
    api_url = config.server + 'api/create_internal_probe.php'
    api_user = config.creds['username']
    api_password = config.creds['password']
    customer_id = config.client_id

    if customer_id == "AIR_001" or not customer_id:
        key = config.load_key()
        with open("data.json", "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data).decode()
        data = json.loads(decrypted_data)

        customer_id = input('Enter your customer ID: ')
        data['client_id'] = customer_id
        encrypted_data = f.encrypt(json.dumps(data).encode())
        with open("data.json", "wb") as json_file:
            json_file.write(encrypted_data)


wg_ip = subprocess.run(['sudo', 'ip', 'address', 'show', 'dev', 'wg0'], capture_output=True, text=True)
wg_ip = wg_ip.stdout.split('inet ')[1].split('/')[0]

payload_conf = config.payload_conf

payload = {
    'creds': {'user_name': api_user, 'password': api_password},
    'server_data': {'server_ip': wg_ip, 'user_name': payload_conf['username'], 'password': payload_conf['password']},
    'cust_id': customer_id
}
response = requests.post(api_url, json=payload, verify=False)

try:
    data = response.json()
    print('API call successful')
    if data['code'] == 1:
        print('Registered Successfully')
        new_hostname = f"{customer_id}.linkeye_local_probe"
        os.system(f"hostnamectl set-hostname {new_hostname}")

        # update /etc/hosts file
        with open('/etc/hosts', 'r') as f:
            file_lines = f.readlines()

        for i, line in enumerate(file_lines):
            if '127.0.1.1' in line:
                file_lines[i] = f'127.0.1.1\t{new_hostname}\n'
                break

        with open('/etc/hosts', 'w') as f:
            f.writelines(file_lines)
        subprocess.run(['sudo', 'sh', '/home/isp_internal_probe/probe_intial.sh'])
    else:
        print('Registration Failed.Wrong Customer ID entered ')
except:
    print(f'API call failed: {response.text}')
