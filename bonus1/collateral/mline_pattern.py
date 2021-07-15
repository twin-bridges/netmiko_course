"""
cisco3#traceroute
Protocol [ip]:
Target IP address: 10.220.88.28
Ingress traceroute [n]:
Source address or interface: 10.220.88.22
DSCP Value [0]:
Numeric display [n]: y
Timeout in seconds [3]:
Probe count [3]:
Minimum Time to Live [1]:
Maximum Time to Live [30]:
Port Number [33434]:
Loose, Strict, Record, Timestamp, Verbose[none]:
Type escape sequence to abort.
Tracing the route to 10.220.88.28
VRF info: (vrf in name/id, vrf out name/id)
"""
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    "session_log": "traceroute.out",
}

dest_ip = "10.220.88.28"
probes = "3"
commands = [
    ["traceroute", r"Protocol"],
    ["\n", r"Target IP address"],
    [dest_ip, r"Ingress traceroute"],
    ["\n", r"Source address or interface"],
    ["10.220.88.22", r"DSCP Value"],
    ["\n", r"Numeric display"],
    ["y", r"Timeout in seconds"],
    ["\n", r"Probe count"],
    [probes, r"Minimum Time to Live"],
    ["\n", r"Maximum"],
    ["\n", r"Port Number"],
    ["\n", r"Loose"],
    ["\n", ""],
]

start_time = datetime.now()
with ConnectHandler(**device) as ssh_conn:
    print("\n\n")
    print(ssh_conn.find_prompt())
    print("-" * 50)
    output = ssh_conn.send_multiline(commands)
    print(output)
    print("-" * 50)
    print("\n\n")
end_time = datetime.now()
print(f"Execution time: {end_time - start_time}")
