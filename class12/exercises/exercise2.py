import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    debug = True
    device = {
        "device_type": "cisco_ios",
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    net_connect = ConnectHandler(**device)
    print(f"\nCurrent Prompt:\n{net_connect.find_prompt()}\n")

    print("Enter into configuration mode:")
    output = net_connect.config_mode()
    net_connect.clear_buffer()
    print(f"\nCurrent Prompt:\n{net_connect.find_prompt()}\n")

    new_hostname = "cisco4-testing"
    net_connect.write_channel(f"hostname {new_hostname}\n")

    print("Exit configuration mode:")
    output = net_connect.exit_config_mode()

    # Should reset Netmiko's base prompt if you change the hostname
    net_connect.set_base_prompt()

    print(f"\nCurrent Prompt:\n{net_connect.find_prompt()}\n")
