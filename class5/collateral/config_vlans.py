import os
from getpass import getpass
import yaml
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


if __name__ == "__main__":

    # Code so automated tests will run properly
    # Check for environment variable, if that fails, use getpass().
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    device_dict = load_devices()

    arista1 = device_dict["arista1"]
    arista2 = device_dict["arista2"]
    arista3 = device_dict["arista3"]
    arista4 = device_dict["arista4"]

    cfg_changes = ["vlan 500", "name gold500"]

    for device in (arista1, arista2, arista3, arista4):
        device["password"] = password
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(cfg_changes)
        output += net_connect.save_config()
        print(output)
        net_connect.disconnect()
