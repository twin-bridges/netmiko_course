#!/usr/bin/env python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "ssh_config_file": "./my_ssh_config",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show users")

print(output)
