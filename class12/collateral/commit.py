import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    vmx2 = {
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "output.txt",
    }

    with ConnectHandler(**vmx2) as net_connect:

        print("\n\nSend configuration commands to device:")
        cfg_commands = [
            "set system syslog archive size 110k files 3",
            "set system time-zone America/New_York",
        ]
        output = net_connect.send_config_set(cfg_commands)

        divider = "-" * 20
        print(f"\n{divider}\n{output}\n{divider}\n")

        print("Commit change...operation is slow")

        # Standard Commit
        output = net_connect.commit()

        # Commit with a comment
        # output = net_connect.commit(comment="Configuration change using Netmiko")

        # Commit confirm
        # output = net_connect.commit(confirm=True, confirm_delay=3)
        # wait_here = input("Hit enter to continue: ")
        # output = net_connect.commit()

        print(f"\n{divider}\n{output}\n{divider}\n")
        print()
