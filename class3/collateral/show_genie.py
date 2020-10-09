import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command("show ip int brief", use_genie=True)
    # output = net_connect.send_command("show ip arp", use_genie=True)
    pprint(output)
