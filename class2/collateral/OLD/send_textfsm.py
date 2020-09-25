import os
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**cisco3)
output = net_connect.send_command("show ip int brief", use_textfsm=True)
pprint(output)
