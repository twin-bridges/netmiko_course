import os
import logging
from getpass import getpass
from netmiko import ConnLogOnly


# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

log_level = logging.INFO
log_file = "my_output.log"

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "boguspass",
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
    # If connection fails, just move on to the next device
    ssh_conn = ConnLogOnly(log_file=log_file, log_level=log_level, **device)
    if not ssh_conn:
        continue

    print("\n\n")
    print(ssh_conn.find_prompt())
    print("-" * 50)
    output = ssh_conn.send_multiline(commands)
    print(output)
    print("-" * 50)
    print("\n\n")
