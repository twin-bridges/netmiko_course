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

command = "traceroute 10.220.88.28"

with ConnectHandler(**device) as ssh_conn:
    start_time = datetime.now()
    output = ssh_conn.send_command(command, read_timeout=20)
    end_time = datetime.now()
    print()
    print("-" * 50)
    print(output)
    print(f"\n\nExecution time: {end_time - start_time}\n\n")
    print("-" * 50)
    print()
