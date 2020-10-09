# Add logging
# for loop and multiple devices
# four arista switches
# send show ip arp
import os
from getpass import getpass
from netmiko import ConnectHandler

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista3 = {
    "device_type": "arista_eos",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista4 = {
    "device_type": "arista_eos",
    "host": "arista4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (arista1, arista2, arista3, arista4):
    with ConnectHandler(**device) as net_connect:
        device_name = net_connect.find_prompt()
        output = net_connect.send_command("show ip arp")
        print(f"\nDevice: {device_name}:")
        print(output)
        print()
