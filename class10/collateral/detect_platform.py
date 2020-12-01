import os
from getpass import getpass
from netmiko import SSHDetect, ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

base_device = {"device_type": "autodetect", "username": "pyclass", "password": password}

hosts = [
    "cisco3.lasthop.io",
    "nxos1.lasthop.io",
    "vmx1.lasthop.io",
    "arista1.lasthop.io",
]

for hostname in hosts:
    device = base_device.copy()
    device["host"] = hostname
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    # Name of the best device_type to use further
    print(best_match)

# Connect to the very last device
device["device_type"] = best_match
with ConnectHandler(**device) as connection:
    print()
    print("Full SSH Connection:")
    print(connection.find_prompt())
