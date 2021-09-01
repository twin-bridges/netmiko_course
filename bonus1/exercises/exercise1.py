import os
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler, ReadTimeout

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass    ()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}

try:
    ssh_conn = ConnectHandler(**device)
    start = datetime.now()
    show_tech = ssh_conn.send_command("show tech-support", read_timeout=5)
except ReadTimeout:
    end = datetime.now()
    print("\nProgram failed with ReadTimeout Exception.\n")
    print(f"Execution time: {end - start}")
    print("\n")
