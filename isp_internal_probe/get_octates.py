from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from easysnmp import Session, exceptions as easysnmp_exceptions
import mysql.connector
from datetime import datetime
from config_class import config
import subprocess

host = config.mysql_conf["host"]
database = config.mysql_conf["database"]
user = config.mysql_conf["user"]
password = config.mysql_conf["password"]
port = config.mysql_conf["port"]
auth_plugin = config.mysql_conf["auth_plugin"]

config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database,
    'port': port,
    'auth_plugin': auth_plugin
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def snmp_get_push_db_for_palo_alto(device_ip, device_id, community, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, public_ip, ifindex, isp_wan_id):
    try:
        in_oid = f'1.3.6.1.2.1.31.1.1.1.6.{ifindex}'
        out_oid = f'1.3.6.1.2.1.31.1.1.1.10.{ifindex}'

        if snmp_version == 2:
            session = Session(hostname=device_ip, community=community, version=2, timeout=2)
        elif snmp_version == 3:
            if security_level == "0":
                session = Session(hostname=device_ip, version=3, security_username=community, timeout=2)
            elif security_level == "1":
                session = Session(
                    hostname=device_ip, version=3, security_username=community, 
                    auth_protocol=auth_type, auth_password=auth_password, security_level='authNoPriv', timeout=2
                )
            elif security_level == "2":
                session = Session(
                    hostname=device_ip, version=3, security_username=community, 
                    auth_protocol=auth_type, auth_password=auth_password,
                    privacy_protocol=privacy_type, privacy_password=privacy_password, security_level='authPriv', timeout=2
                )
        else:
            print(f"Unsupported SNMP version: {snmp_version}")
            return device_ip, public_ip, device_id, ifindex, None, None, isp_wan_id

        in_result = session.get(in_oid)
        out_result = session.get(out_oid)
        return device_ip, public_ip, device_id, ifindex, in_result.value, out_result.value, isp_wan_id
    # except easysnmp_exceptions.EasySNMPTimeoutError:
    #     print(f"Timeout error while connecting to {device_ip}")
    #     return device_ip, public_ip, device_id, ifindex, None, None, isp_wan_id
    except Exception as e:
        print(f"Error while performing SNMP operation on {device_ip}: {e}")
        return device_ip, public_ip, device_id, ifindex, None, None, isp_wan_id
    
def snmp_get_push_db(device_ip, device_id, community, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, public_ip, ifindex, isp_wan_id):
    try:
        in_oid = f'1.3.6.1.2.1.2.2.1.10.{ifindex}'
        out_oid = f'1.3.6.1.2.1.2.2.1.16.{ifindex}'

        if snmp_version == 2:
            session = Session(hostname=device_ip, community=community, version=2, timeout=2)
        elif snmp_version == 3:
            if security_level == "0":
                session = Session(hostname=device_ip, version=3, security_username=community, timeout=2)
            elif security_level == "1":
                session = Session(
                    hostname=device_ip, version=3, security_username=community, 
                    auth_protocol=auth_type, auth_password=auth_password, security_level='authNoPriv', timeout=2
                )
            elif security_level == "2":
                session = Session(
                    hostname=device_ip, version=3, security_username=community, 
                    auth_protocol=auth_type, auth_password=auth_password,
                    privacy_protocol=privacy_type, privacy_password=privacy_password, security_level='authPriv', timeout=2
                )
        else:
            print(f"Unsupported SNMP version: {snmp_version}")
            return device_ip, public_ip, device_id, ifindex, None, None, isp_wan_id

        in_result = session.get(in_oid)
        out_result = session.get(out_oid)
        return device_ip, public_ip, device_id, ifindex, in_result.value, out_result.value, isp_wan_id
    # except easysnmp_exceptions.EasySNMPTimeoutError:
    #     print(f"Timeout error while connecting to {device_ip}")
    #     return device_ip, public_ip, device_id, ifindex, None, None, isp_wan_id
    except Exception as e:
        print(f"Error while performing SNMP operation on {device_ip}: {e}")
        return device_ip, public_ip, device_id, ifindex, None, None, isp_wan_id
    


def snmp_get_device(device_ip, device_id, community, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, vendor, type, oid_public_ip_list):
    if vendor == "Palo Alto" and type == "Firewall":
        with ThreadPoolExecutor(max_workers=48) as executor:
            results = executor.map(lambda oid_public_ip: snmp_get_push_db_for_palo_alto(device_ip, device_id, community, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, *oid_public_ip),
                                oid_public_ip_list)
        return list(results)
    else:
        with ThreadPoolExecutor(max_workers=48) as executor:
            results = executor.map(lambda oid_public_ip: snmp_get_push_db(device_ip, device_id, community, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, *oid_public_ip),
                                oid_public_ip_list)
        return list(results)


def worker(device_info):
    device_ip, community, device_id, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, vendor, type, ifindex_public_ip_list = device_info
    oid_public_ip_list = [(public_ip, ifindex, isp_wan_id) for ifindex, public_ip, isp_wan_id in ifindex_public_ip_list]
    return snmp_get_device(device_ip, device_id, community, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password,vendor, type,  oid_public_ip_list)

def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Start Time:", current_time)

    qry = f""" SELECT fn_edge_devices.device_id, fn_edge_devices.device_ip, fn_edge_devices.snmp_str, fn_edge_devices.snmp_version, fn_edge_devices.security_level, fn_edge_devices.auth_type, fn_edge_devices.auth_password, fn_edge_devices.privacy_type, fn_edge_devices.privacy_password, fn_edge_devices.vendor, fn_edge_devices.type
                FROM fn_isp_details, fn_edge_devices
                WHERE  fn_isp_details.edge_device_id = fn_edge_devices.device_id"""
    cursor.execute(qry)
    results = cursor.fetchall()

    device_info = {}
    for row in results:
        device_id, device_ip, community, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, vendor, type = row

        ifindex_qry = f"""SELECT fn_isp_details.if_index, fn_isp_details.internal_ip, fn_isp_details.isp_wan_id
                          FROM fn_isp_details WHERE fn_isp_details.edge_device_id={device_id} AND fn_isp_details.isp_wan_id != -1"""
        cursor.execute(ifindex_qry)
        ifResults = cursor.fetchall()

        ifindex_public_ip_list = [(ifindex, internal_ip, isp_wan_id) for ifindex, internal_ip, isp_wan_id in ifResults]

        device_info[device_ip] = (device_ip, community, device_id, snmp_version, security_level, auth_type, auth_password, privacy_type, privacy_password, vendor, type, ifindex_public_ip_list)

    device_info_list = [info for info in device_info.values()]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(worker, device_info_list))

    flattened_results = [item for sublist in results for item in sublist]

    for res in flattened_results:
        device_ip, public_ip, device_id, ifindex, in_octates, out_octates, isp_wan_id = res
        if in_octates is not None and out_octates is not None:
            delete_qry = f"""DELETE FROM fn_latest_in_out_octates WHERE isp_wan_id='{isp_wan_id}' AND created_at <= NOW() - INTERVAL 3 MINUTE"""
            cursor.execute(delete_qry)
            insert_qry = f"""INSERT INTO fn_latest_in_out_octates (`public_ip`, `device_ip`, `ifindex`, `in_octates`,
            `out_octates`, `isp_wan_id`) VALUES ('{public_ip}', '{device_ip}', {ifindex}, {in_octates}, {out_octates}, '{isp_wan_id}')"""
            # print(insert_qry)
            cursor.execute(insert_qry)
            conn.commit()

    cursor.close()
    conn.close()

    subprocess.run(['python3', 'process_octate_push_to_core.py'])
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Finished Time:", current_time)


if __name__ == "__main__":
    main()
