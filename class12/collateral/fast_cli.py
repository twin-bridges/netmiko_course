import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": True,
}

with ConnectHandler(**my_device) as net_connect:

    print(f"\n\n{net_connect.find_prompt()}\n\n")
    print(f"Fast CLI state: {net_connect.fast_cli}")
    print(f"Global Delay Factor state: {net_connect.global_delay_factor}")

    output = net_connect.send_command("show ip int brief")
    print()
    print("-" * 20)
    print(output)
    print()
