from config_class import config
import requests
import subprocess
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if __name__ == "__main__":
    api_path = config.server + "api/check_config_change_msp.php"
    payload = {
        "creds": config.creds,
        "cust_id": config.client_id,
    }
    
    api_response = requests.post(api_path, json=payload, verify=False)
    response = api_response.json()

    if response['code'] == 1:
        try:
            # Run the shell script
            subprocess.run(['sh', "probe_intial.sh"], check=True)
            # subprocess.run(['sh', 'test.sh'], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors, if the script returns a non-zero exit code
            print(f"Error running the script: {e}")
        else:
            print("Script executed successfully")
    else:
        print("There is no config changes done")
