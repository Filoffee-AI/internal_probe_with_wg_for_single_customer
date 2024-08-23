import json
from cryptography.fernet import Fernet
import keyring

from keyrings.alt import file

keyring.set_keyring(file.PlaintextKeyring())

class Config:

    def load_key(self):
        # return open("secret.key", "rb").read()
        key = keyring.get_password("Gyan_LinkEye", "Key")
        if key:
            return key
        else:
            return "Password not found in keyring."

    def decrypt_json(self, encrypted_file_path, key):
        f = Fernet(key)
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = f.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

    def __init__(self):
        key = self.load_key()
        config = self.decrypt_json("data.json", key)

        self.customer_ids = config['cust_id']
        self.creds = config['creds']
        self.server = config['server']
        self.mysql_conf = config['mysql_conf']
        self.influx_conf = config['influx_conf']
        self.telegraf_conf = config['telegraf_conf']
        self.headers = config['headers']
        self.client_id = config['client_id']
        self.wg_conf = config['wg_conf']
        self.payload_conf = config['payload_creds']
        # print(config)


config = Config()
