from config_class import config
import sys
from influxdb_client import InfluxDBClient
import pytz
import datetime
import json
from config_class import config

device_ip = sys.argv[1]
# public_ip = sys.argv[2]
time_obj = datetime.datetime.now(tz=pytz.UTC)

org = config.influx_conf["org"]
token = config.influx_conf["token"]
url = config.influx_conf["url"]

output = {}
time2 = time_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
time1 = (time_obj - datetime.timedelta(minutes=1)).strftime('%Y-%m-%dT%H:%M:%S.%f')

# print(f'Checking Health of Firewall Devices in interval between {time1} and {time2}')

query = f'from(bucket: "Firewall_test") \
|> range(start: {time1}Z, stop: {time2}Z ) \
|> filter(fn: (r) => r["_measurement"] == "Filo_nms Firewall") \
|> filter(fn: (r) => r["_field"] == "CPU_Utilization_FW" or r["_field"] == "Memory_Capacity_FW" or r["_field"] == "Memory_Usage_FW" or r["_field"] == "Uptime_FW") \
|> filter(fn: (r) => r["agent_host"] == "{device_ip}")'

client = InfluxDBClient(url=url, token=token, org=org)
result = client.query_api().query(query)
# print(result)

total_cpu = 8
try:
    for table in result:
        for record in table.records:
            if record.get_field() == "CPU_Utilization_FW":
                cpu = record.get_value()
                time_cpu_utc = record.get_time()

            elif record.get_field() == "Uptime_FW":
                uptime = record.get_value()

            elif record.get_field() == "Memory_Capacity_FW":
                mem_cap = record.get_value()

            elif record.get_field() == "Memory_Usage_FW":
                mem_usg = record.get_value()

    uptime1 = (uptime / 100)  # convert into Seconds


    def format_uptime(uptime):
        year, uptime = divmod(uptime, 31536000)
        month, uptime = divmod(uptime, 2592000)
        day, uptime = divmod(uptime, 86400)
        hour, uptime = divmod(uptime, 3600)
        minute, second = divmod(uptime, 60)
        return year, month, day, hour, minute, second


    uptime_in_seconds = uptime1
    formatted_uptime = format_uptime(uptime_in_seconds)
    # print("Uptime into format of YYMMDDHHMMSS :",formatted_uptime) #convert uptime into YYMMDDHHMMSS

    per_mem = mem_usg / mem_cap * 100  # percentage memory usage
    per_cpu = (cpu / total_cpu) * 100  # percentage CPU usage

    output['memory_usage'] = mem_usg
    output['cpu_usage'] = cpu
    output['message'] = f'''CPU Usage:{cpu}%  Mem Usage:{mem_usg}%'''

    # print("cpu :" + str(cpu)+" Memory Percentage Usage :"+str(per_mem)+" at "+str(time_cpu_utc))
    print(json.dumps(output))

except NameError:
    print("Data is Not Available.....Check host Again")
