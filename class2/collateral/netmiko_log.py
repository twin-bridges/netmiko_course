import os
from netmiko import ConnectHandler
from getpass import getpass

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)
print(net_connect.find_prompt())
net_connect.disconnect()
