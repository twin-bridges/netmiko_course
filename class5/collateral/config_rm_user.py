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

    cisco3 = device_dict["cisco3"]

    for device in (cisco3,):
        device["password"] = password
        net_connect = ConnectHandler(**device)

        cmd = "no username my_user"
        output = net_connect.config_mode()
        output += net_connect.send_command_timing(
            cmd, strip_prompt=False, strip_command=False
        )
        if "confirm" in output:
            output += net_connect.send_command_timing(
                "y", strip_prompt=False, strip_command=False
            )
        output += net_connect.exit_config_mode()
        output += net_connect.save_config()
        print(output)
        net_connect.disconnect()
