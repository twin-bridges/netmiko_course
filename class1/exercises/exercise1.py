import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

net_connect = ConnectHandler(
    device_type="cisco_nxos",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=password,
)

print(net_connect.find_prompt())
