import os
from getpass import getpass
from netmiko import ConnectHandler, NetmikoAuthenticationException


def netmiko_connect(device):
    """
    Successful connection returns: (True, connect_obj)

    Failed authentication returns: (False, None)
    """
    try:
        net_connect = ConnectHandler(**device)
        return (True, net_connect)
    except NetmikoAuthenticationException:
        return (False, None)


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    nxos2 = {
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
    }

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if not connect_status:
        print("\nAuthentication failed...retrying\n\n")
        nxos2["password"] = password

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if connect_status:
        print("\nAuthenticated successfully")
        output = net_connect.send_command("show ip arp vrf management")
        print(f"\n{output}\n")

    print()
