import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    "session_log": "traceroute.out",
}

command = "show tech-support"
ssh_conn = ConnectHandler(**device)

# Gather the entire output
start_time = datetime.now()
output = ssh_conn.send_command_timing(
    command, last_read=10, read_timeout=180, strip_prompt=False
)
end_time = datetime.now()
ssh_conn.disconnect()

print("\n\n")
print("-" * 80)
print(output)
print("-" * 80)
print("\n\n")
print(f"Exec time: {end_time - start_time}")
print("\n\n")
