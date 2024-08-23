import subprocess
import re
import requests
import sys
import json
import datetime

def ping(ip, count=5):
    ping_cmd = ['ping', '-c', str(count), '-W', str(1), ip]  # For Linux/MacOS

    try:
        output = subprocess.check_output(ping_cmd, universal_newlines=True)

        latencies = re.findall(r"time=(\d+(?:\.\d+)?)", output)
        packet_loss_match = re.search(r'(\d+(?:\.\d+)?)%\s+packet loss', output)

        if latencies and packet_loss_match:
            packet_loss = packet_loss_match.group(1)
            latencies = [float(latency) for latency in latencies]
            avg_latency = sum(latencies) / len(latencies)

            squared_diff_sum = sum((latency - avg_latency) ** 2 for latency in latencies)
            jitter = (squared_diff_sum / len(latencies)) ** 0.5

            status = 1 if packet_loss != '100' else 0

            return {
                'packet_loss': packet_loss,
                'min_latency': min(latencies),
                'max_latency': max(latencies),
                'avg_latency': avg_latency,
                'jitter': jitter,
                'status': status
            }
        else:
            return {
                'packet_loss': 100,
                'min_latency': 0,
                'max_latency': 0,
                'avg_latency': 0,
                'jitter': 0,
                'status': 0
            }
    except subprocess.CalledProcessError:
        return {
            'packet_loss': 100,
            'min_latency': 0,
            'max_latency': 0,
            'avg_latency': 0,
            'jitter': 0,
            'status': 0
        }


if __name__ == "__main__":
    cust_id = sys.argv[1]
    device_id = sys.argv[2]
    device_ip = sys.argv[3]
    username = sys.argv[4]
    password = sys.argv[5]
    server = sys.argv[6]

    host = ping(device_ip)

    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    device_status = {
        "client_id": cust_id,
        "device_id": device_id,
        "device_ip": device_ip,
        "jitter": host['jitter'],
        "latency": host['avg_latency'],
        "packet_loss": host['packet_loss'],
        "status": host['status'],
        "time": start_time
    }

    json_data = {
        "creds": {
            "username": username,
            "password": password
        },
        "device_status": device_status
    }
    api_path = server + "api/push_edge_device_status.php"
    api_response = requests.post(api_path, json=json_data, verify=False)

    try:
        data = api_response.json()
        print("Info: Data Pushed to Server Successfully", data)
    except json.JSONDecodeError as e:
        print("Error: Error in Pushing Data to Server:", e)
