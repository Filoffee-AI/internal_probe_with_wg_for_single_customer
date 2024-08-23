import subprocess
import re
import requests
import sys
import json
import datetime


def ping(ip, count=5):
    # Check the platform to determine the appropriate ping command
    ping_cmd = ['ping', '-c', str(count), ip]  # For Linux/MacOS

    try:
        # Execute the ping command and capture the output
        output = subprocess.check_output(ping_cmd, universal_newlines=True)
        # print(output)
        # Parse the output to extract latency, jitter, and packet loss
        latencies = re.findall(r"time=(\d+(?:\.\d+)?)", output)
        # packet_loss_match = re.search(r"(\d+(?:\.\d+)?%)\s+loss", output)
        packet_loss_match = re.search(r'(\d+(?:\.\d+)?)%\s+packet loss', output)
        # print(latencies)
        # print(packet_loss_match)

        if latencies and packet_loss_match:
            packet_loss = packet_loss_match.group(1)
            latencies = [float(latency) for latency in latencies]
            avg_latency = sum(latencies) / len(latencies)

            # Calculate jitter
            squared_diff_sum = sum((latency - avg_latency) ** 2 for latency in latencies)
            jitter = (squared_diff_sum / len(latencies)) ** 0.5

            return {
                'packet_loss': packet_loss,
                'min_latency': min(latencies),
                'max_latency': max(latencies),
                'avg_latency': avg_latency,
                'jitter': jitter
            }
        else:
            return {
                'packet_loss': 100,
                'min_latency': 0,
                'max_latency': 0,
                'avg_latency': 0,
                'jitter': 0
            }
    except subprocess.CalledProcessError:
        return {
            'packet_loss': 100,
            'min_latency': 0,
            'max_latency': 0,
            'avg_latency': 0,
            'jitter': 0
        }


if __name__ == "__main__":
    isp_wan_id = sys.argv[1]
    cust_id = sys.argv[2]
    circuit_id = sys.argv[3]
    location = sys.argv[4]
    isp_public_ip = sys.argv[5]
    vendor = sys.argv[6]
    server = sys.argv[7]
    username = sys.argv[8]
    password = sys.argv[9]
    dg_ip = sys.argv[10]

    status = 0
    dg_status = 0

    host = ping(isp_public_ip)
    # print(host)
    if host['packet_loss'] != 100:
        status = 1

    dg = ping(dg_ip)
    if dg['packet_loss'] != 100:
        dg_status = 1

    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    json_data = {
        "creds": {
            "username": username,
            "password": password
        },
        "isp_data": {
            "isp_wan_id": isp_wan_id,
            "client_id": cust_id,
            "circuit_id": circuit_id,
            "public_ip": isp_public_ip,
            "min_rtt": host['min_latency'],
            "avg_rtt": host['avg_latency'],
            "max_rtt": host['max_latency'],
            "jitter": host['jitter'],
            "packet_loss": host['packet_loss'],
            "status": status,
            "dg_ip": dg_ip,
            "dg_status": dg_status,
            "dg_min_rtt": dg['min_latency'],
            "dg_max_rtt": dg['max_latency'],
            "dg_avg_rtt": dg['avg_latency'],
            "dg_jitter": dg['jitter'],
            "dg_packet_loss": dg['packet_loss'],
            "time": start_time
        }
    }
    # print(json_data)
    api_path = server + "api/push_isp_data.php"
    api_response = requests.post(api_path, json=json_data, verify=False)

    try:
        data = api_response.json()
        # print("Info: Data Pushed to Server Successfully", data)
    except json.JSONDecodeError as e:
        print("Error: Error in Pushing Data to Server:", e)
