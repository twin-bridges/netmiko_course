import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}

with ConnectHandler(**my_device) as net_connect:

    # Multiply delay by four for this particular method
    output = net_connect.send_command("show ip int brief", delay_factor=5, max_loops=1000)
    print(output)

