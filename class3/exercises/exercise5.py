import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)
output = net_connect.send_command(
    "show vlan", use_ttp=True, ttp_template="show_vlan.ttp"
)
net_connect.disconnect()

print()
print("VLAN Table:")
print("-" * 18)
pprint(output)
print()

# Strip outer lists
data = output[0][0]
for vlan_dict in data:
    if vlan_dict["vlan_id"] == "7":
        print()
        print(f"VLAN ID: {vlan_dict['vlan_id']}")
        print(f"VLAN name: {vlan_dict['vlan_name']}")
        print()
