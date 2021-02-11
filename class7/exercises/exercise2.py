from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException


def netmiko_connect(device):
    """
    Successful connection returns: (True, connect_obj)

    Failed authentication returns: (False, None)
    """
    try:
        net_connect = ConnectHandler(**device)
        return (True, net_connect)
    except NetmikoAuthenticationException:
        print("\nAuthentication failed")
        return (False, None)
    except NetmikoTimeoutException:
        print("\nConnection failed")
        return (False, None)


if __name__ == "__main__":

    nxos2 = {
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
        "port": 8022,
    }

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if not connect_status:
        print("\nInitial connection failed...retrying\n\n")
        nxos2["password"] = getpass()
        nxos2["port"] = 22

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if connect_status:
        print("\nAuthenticated successfully")
        output = net_connect.send_command("show ip arp vrf management")
        print(f"\n{output}\n")

    print()
