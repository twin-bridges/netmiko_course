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
    # Set fast_cli=False to get proper behavior out of delay_factor
    "fast_cli": False,
}

with ConnectHandler(**my_device) as net_connect:
    # Set delay_factor=5 to get 1-second per loop so here Netmiko will wait up to 1000 seconds
    output = net_connect.send_command("show run", delay_factor=5, max_loops=1000)
    print(output)
