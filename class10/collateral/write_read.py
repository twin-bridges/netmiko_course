import os
import time
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "output.txt",
}

with ConnectHandler(**my_device) as net_connect:

    # Send command down the channel - don't forget the enter!
    net_connect.write_channel("show ip int brief\n")

    # You probably can't read right away - your Python program is faster than the device (so sleep)
    time.sleep(1)
    output = net_connect.read_channel()
    print(output)
    print()

    print("-" * 20)
    print()

    # You can do multiple interactions
    net_connect.write_channel("config term\n")
    time.sleep(1)
    output = net_connect.read_channel()
    net_connect.write_channel("end\n")
    time.sleep(1)
    output += net_connect.read_channel()
    print(output)
