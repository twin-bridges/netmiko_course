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

    filename = "test_cf.txt"
    cmd_list = [
        [f"del flash:/{filename}", r"Delete filename"],
        ["\n", r"confirm"],
        ["y", r"#"],
    ]

    output = net_connect.send_multiline(cmd_list)
    print(output)
