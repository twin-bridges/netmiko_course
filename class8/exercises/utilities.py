from netmiko import ConnectHandler
import yaml


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def ssh_conn(device_name, device_dict, cmd=None):
    with ConnectHandler(**device_dict) as net_connect:
        if cmd is None:
            return net_connect.find_prompt()
        else:
            output = net_connect.send_command(cmd)
            return (device_name, output)
