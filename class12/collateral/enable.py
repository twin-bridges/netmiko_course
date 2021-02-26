import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


def lower_privileges(net_connect):
    net_connect.exit_enable_mode()
    print("*" * 40)
    print()
    print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
    show_current_priv(net_connect)


def show_current_priv(net_connect):
    output = net_connect.send_command("show priv")
    print(f"Current Privilege Level: {output}")


if __name__ == "__main__":

    my_device = {
        "device_type": "cisco_ios",
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": password,
        "secret": password,
    }

    with ConnectHandler(**my_device) as net_connect:

        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        show_current_priv(net_connect)

        # Drop to privilege level1
        lower_privileges(net_connect)

        # Use 'enable()' method to raise privileges. This will automatically handle the password
        # must have 'secret' argument set in the device dictionary.
        net_connect.enable()
        print("*" * 40)
        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        show_current_priv(net_connect)

        # Try again - go back to priv level1
        lower_privileges(net_connect)

        # Now call 'enable', but feed in a 'cmd'
        net_connect.enable(cmd="enable 15")
        print("*" * 40)
        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        show_current_priv(net_connect)
