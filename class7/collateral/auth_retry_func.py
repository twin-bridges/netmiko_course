import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException


def try_passwords(device, passwords=None):
    """
    Retry using all of the passwords provided.

    passwords is an iterator of passwords to try.
    """
    if passwords is None:
        passwords = []
    for passwd in passwords:
        device["password"] = passwd
        try:
            net_connect = ConnectHandler(**device)
            break
        except NetmikoAuthenticationException:
            continue
    else:
        # nobreak
        raise NetmikoAuthenticationException("No valid password found.")
    return net_connect


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
    }

    real_password = password
    password_list = ["invalid1", "invalid2", real_password]

    net_connect = try_passwords(cisco3, password_list)
    output = net_connect.send_command("show ip arp")

    print(f"\n{output}\n")
