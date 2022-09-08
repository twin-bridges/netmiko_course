import os
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**arista1) as net_connect:
    show_vlan = net_connect.send_command("show vlan", use_textfsm=True)

    print()
    print("VLAN Table:")
    print("-" * 18)
    pprint(show_vlan)
    print()

    for vlan_dict in show_vlan:
        if vlan_dict["vlan_id"] == "7":
            print()
            print(f"VLAN ID: {vlan_dict['vlan_id']}")
            print(f"VLAN name: {vlan_dict['name']}")
            print()
