from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
}

with ConnectHandler(**device) as net_connect:

    # cisco3#del flash:/ex1.cfg
    # Delete filename [ex1.cfg]?
    # Delete bootflash:/ex1.cfg? [confirm]y
    # cisco3#

    filename = "test1_vlan.txt"
    cmd_list = [
        f"del flash:/{filename}",
        "\n",
        "y",
    ]

    output = net_connect.send_multiline_timing(cmd_list)
    print(output)
