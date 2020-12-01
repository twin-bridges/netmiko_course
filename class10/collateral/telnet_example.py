import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco1 = {
    "device_type": "cisco_ios_telnet",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**cisco1)
print(net_connect.find_prompt())
net_connect.disconnect()
