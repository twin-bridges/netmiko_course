import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    # Set fast_cli=False to get proper behavior out of delay_factor
    "fast_cli": False,
}

start_time = datetime.now()
with ConnectHandler(**my_device) as net_connect:
    # Set delay_factor=5 to get 1-second per loop so here Netmiko will wait up to 1000 seconds
    output = net_connect.send_command("show run", delay_factor=5, max_loops=1000)
    print(output)
end_time = datetime.now()
exec_time = end_time - start_time

print(f"\n\nExecution Time: {exec_time}\n")
