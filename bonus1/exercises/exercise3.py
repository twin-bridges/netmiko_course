from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler, ReadTimeout

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
    "session_log": "traceroute.out",
}


command = "show tech-support"
ssh_conn = ConnectHandler(**device)

try:
    # Timeout in 15 seconds
    start_time = datetime.now()
    output = ssh_conn.send_command_timing(command, last_read=10, read_timeout=15)
except ReadTimeout:
    end_time = datetime.now()
    print(f"Timed out: {end_time - start_time}")

# Gather the entire output
start_time = datetime.now()
output = ssh_conn.send_command_timing(
    command, last_read=10, read_timeout=120, strip_prompt=False
)
end_time = datetime.now()

print("-" * 80)
print(output)
print("-" * 80)
print("\n\n")
print(f"Exec time: {end_time - start_time}")

ssh_conn.disconnect()
