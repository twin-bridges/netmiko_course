import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException


# Code so automated tests will run properly
password = (
    os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "invalid"
}

output = ""
try:
    net_connect = ConnectHandler(**cisco3)
    output = net_connect.send_command("show ip arp")
except NetmikoAuthenticationException:
    print("Initial auth failed")
    cisco3["password"] = password
    net_connect = ConnectHandler(**cisco3)
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
