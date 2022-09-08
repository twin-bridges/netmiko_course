"""
Reference ping output:

cisco3#ping
Protocol [ip]:
Target IP address: 8.8.8.8
Repeat count [5]: 100
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 100, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/4 ms
"""
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}

commands = [
    ("ping", "Protocol"),
    ("\n", "Target"),
    ("8.8.8.8", "Repeat count"),
    ("100", "Datagram size"),
    ("\n", "Timeout"),
    ("\n", "Extended commands"),
    ("\n", "Sweep range"),
    ("\n", "#"),
]
for device in (cisco3, cisco4):
    with ConnectHandler(**device) as ssh_conn:
        print("\n\n")
        print(ssh_conn.find_prompt())
        print("-" * 50)
        output = ssh_conn.send_multiline(commands)
        print(output)
        print("-" * 50)
        print("\n\n")
