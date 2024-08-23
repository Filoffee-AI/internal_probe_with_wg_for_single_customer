from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import mysql.connector
import requests
from config_class import config


def get_db_connection():
    # Get a new database connection
    myconfig = {
        'host': config.mysql_conf["host"],
        'user': config.mysql_conf["user"],
        'password': config.mysql_conf["password"],
        'database': config.mysql_conf["database"],
    }
    return mysql.connector.connect(**myconfig)


def calculate_bw_push(isp_wan_id, public_ip):
    conn = get_db_connection()  # Get a new connection for the process
    cursor = conn.cursor()
    octate_sql = f"""select public_ip, device_ip, in_octates, out_octates, created_at from fn_latest_in_out_octates WHERE isp_wan_id='{isp_wan_id}' ORDER BY id DESC limit 2"""
    cursor.execute(octate_sql)
    octate_res = cursor.fetchall()

    if len(octate_res) == 2:
        n1_data, n2_data = octate_res

        n1_in_octates = n1_data[2]
        n2_in_octates = n2_data[2]

        n1_out_octates = n1_data[3]
        n2_out_octates = n2_data[3]

        n1_time = n1_data[4]
        n2_time = n2_data[4]

        time_diff = n1_time - n2_time
        seconds_difference = time_diff.total_seconds()
        # print(f'''Seconds{seconds_difference}''')

        # Skip if counter resets
        if n1_in_octates < n2_in_octates or n1_out_octates < n2_out_octates:
            return

        in_diff = n1_in_octates - n2_in_octates
        bandwidthIn = in_diff / seconds_difference * 8.0 / 1048576.0

        out_diff = n1_out_octates - n2_out_octates
        bandwidthOut = out_diff / seconds_difference * 8.0 / 1048576.0

        # print(n1_in_octates, n2_in_octates, bandwidthIn, seconds_difference)
        # print(n1_out_octates, n2_out_octates, bandwidthOut, seconds_difference)

        unix_epoch_time = n1_time.timestamp()

        info_arr = []
        info = {}
        info['isp_wan_id'] = isp_wan_id
        info['public_ip'] = public_ip
        info['in_band_width'] = bandwidthIn
        info['out_band_width'] = bandwidthOut
        info["time_stamp"] = unix_epoch_time
        info_arr.append(info)

        try:
            dict = {
                "creds": config.creds,
                "cust_id": config.client_id,
                "isp_stats": info_arr,
            }

            # Send data to the API
            # print(isp_stats)
            api_path = config.server + "api/push_isp_statistics_with_time_stamp_msp.php"
            api_response = requests.post(api_path, json=dict, verify=False)
            api_response.raise_for_status()
            # print(f'API response: {api_response.json()}')
        except Exception as e:
            print(f'Error while pushing data to API: {e} for device {public_ip}')
    cursor.close()
    conn.close()


def worker(ip_data):
    isp_wan_id, public_ip = ip_data  # Unpack the tuple
    calculate_bw_push(isp_wan_id, public_ip)


def main():
    conn = get_db_connection()
    cursor = conn.cursor()
    ips_sql = "SELECT isp_wan_id, public_ip FROM fn_isp_details WHERE if_index != 'None' AND isp_wan_id GROUP BY isp_wan_id, public_ip"
    cursor.execute(ips_sql)
    ips_res = cursor.fetchall()
    cursor.close()
    conn.close()

    # Use ThreadPoolExecutor for database fetching which is I/O bound
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(worker, ips_res)


if __name__ == "__main__":
    main()
