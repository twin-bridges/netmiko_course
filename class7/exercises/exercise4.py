import os
from getpass import getpass
from netmiko import ConnLogOnly


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    # DNS failure
    vmx1 = {
        "name": "vmx1",
        "device_type": "juniper_junos",
        "host": "invalid.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Invalid Port
    vmx2 = {
        "name": "vmx2",
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "port": 8022,
    }

    # Invalid password
    nxos1 = {
        "name": "nxos1",
        "device_type": "cisco_nxos",
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
    }

    # Valid - should connect
    nxos2 = {
        "name": "nxos2",
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    for device in (vmx1, vmx2, nxos1, nxos2):
        device_name = device.pop("name")
        net_connect = ConnLogOnly(**device)
        if net_connect:
            print("\nSuccessfully connected to device:")
            print("-" * 20)
            print(net_connect.find_prompt())
            print("\n\n")
