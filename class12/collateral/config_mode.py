import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    debug = True
    cisco4 = {
        "device_type": "cisco_ios",
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    vmx2 = {
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    my_device = vmx2

    with ConnectHandler(**my_device) as net_connect:

        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")

        print("Enter into configuration mode:")
        output = net_connect.config_mode()
        if debug:
            divider = "-" * 20
            print(f"\n{divider}\n{output}\n{divider}\n")
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        print()

        print("Exit configuration mode:")
        output = net_connect.exit_config_mode()
        if debug:
            divider = "-" * 20
            print(f"\n{divider}\n{output}\n{divider}\n")
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        print()
