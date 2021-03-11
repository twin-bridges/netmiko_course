import os
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": True,
}

net_connect = ConnectHandler(**my_device)

try:
    # Command that send_command will fail on
    print(f"\n\nFast CLI state: {net_connect.fast_cli}")
    print(f"Global Delay Factor state: {net_connect.global_delay_factor}")
    start_time = datetime.now()
    output = net_connect.send_command("conf t")
finally:
    end_time = datetime.now()
    print(f"\nCommand execution time: {end_time - start_time}\n")
