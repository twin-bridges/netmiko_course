import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
my_device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command("show lldp neighbors detail", use_genie=True)
    output = output["interfaces"]
    for intf_name, v in output.items():
        print()
        print(f"Local Intf: {intf_name}")
        print("-" * 12)
        neighbor_dict = v["port_id"][intf_name]["neighbors"]
        for neighbor_name, neighbor_data in neighbor_dict.items():
            remote_port = neighbor_data["port_description"]
            mgmt_ip = neighbor_data["management_address_v4"]
            print(f"Neighbor: {neighbor_name}")
            print(f"  Remote Port: {remote_port}")
            print(f"  MGMT IP: {mgmt_ip}")
            print("-" * 12)
