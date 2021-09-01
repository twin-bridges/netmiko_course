from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
    "session_log": "traceroute.out",
}

command = "traceroute 8.8.8.8"

with ConnectHandler(**device) as ssh_conn:
    try:
        start_time = datetime.now()
        # output = ssh_conn.send_command_timing(command)
        output = ssh_conn.send_command_timing(command, last_read=5, read_timeout=15)
    finally:
        end_time = datetime.now()
        print()
        print("-" * 50)
        print(f"\n\nExecution time: {end_time - start_time}\n\n")
        print("-" * 50)
        print()
