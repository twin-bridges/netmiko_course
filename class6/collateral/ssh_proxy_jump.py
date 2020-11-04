#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "ssh_config_file": "/home/kbyers/.ssh/ssh_config_proxyjump",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show users")

print(output)
