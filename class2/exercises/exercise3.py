import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


cisco3 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

cisco4 = {
    "device_type": "cisco_xe",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (cisco3, cisco4):
    with ConnectHandler(**device) as net_connect:
        start_prompt = net_connect.find_prompt()
        net_connect.send_command_timing("disable")
        end_prompt = net_connect.find_prompt()
        print(f"\nStarting prompt: {start_prompt}")
        print(f"\nEnding prompt: {end_prompt}")
        print()
