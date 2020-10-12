import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


cisco3 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
}

with ConnectHandler(**cisco3) as net_connect:
    # Intentionally do something that will break
    start_prompt = net_connect.find_prompt()

    # Will fail
    # net_connect.send_command("disable")

    # Working with expect_string
    net_connect.send_command("disable", expect_string=r">")

    end_prompt = net_connect.find_prompt()
    print(f"\nStarting prompt: {start_prompt}")
    print(f"\nEnding prompt: {end_prompt}")
    print()
