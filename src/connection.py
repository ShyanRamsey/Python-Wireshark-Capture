from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoAuthenticationException, NetmikoTimeoutException, SSHException 
import os
from dotenv import load_dotenv
from logs.logger import log
import yaml

print("connection started")
class NetworkConnectionManager:
    def __init__(self, path='inventories/inventory.yml'):
        load_dotenv()
        self.path = path
        self.connection = None
        self.devices = {}

    def load_env_variables(self):
        username = os.getenv("DEVICE_USERNAME")
        password = os.getenv("DEVICE_PASS")

        try:
            with open (self.path) as f:
                data = yaml.safe_load(f)
            for device in data.get("devices", []):
                device["username"] = username
                device["password"] = password
                self.devices[device["name"]] = device
            return username, password, self.devices
        except Exception as e:
            log("ENVIRONMENT VARIABLE ERROR", e)
            raise
    def netmiko_connection(self):
        try:
            for name, device in self.devices.items():
                connection_info = device.copy()
                connection_info.pop("name")
                log(name, f"Connecting to {device['host']}")
                self.connection = ConnectHandler(**connection_info)
                running_config = self.connection.send_command("show run")
                with open (f"config/{device['host']}", 'w', encoding='utf-8') as f:
                    f.write(running_config)
        except NetMikoAuthenticationException:
            log(name, "Authentication failed")
            raise
        except NetmikoTimeoutException:
            log(name, "Connection timed out")
        except Exception as e:
            log(name, e)
        finally:
            if self.connection:
                self.connection.disconnect()

if __name__ == "__main__":
    manager = NetworkConnectionManager()
    manager.load_env_variables()
    manager.netmiko_connection()
    