import os
from netmiko import ConnectHandler
from getpass import getpass

# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**nxos1)
output = net_connect.send_command("show version")
print(output)
