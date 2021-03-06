import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}
nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}

config_cmds = ["ip domain-lookup", "ip domain-name bogus.com"]

for device in (nxos1, nxos2):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_set(config_cmds)
        print(f"\n{output}\n")
