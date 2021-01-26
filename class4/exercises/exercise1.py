import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
    # If using send_command_timing, always set fast_cli=False
    "fast_cli": False,
}

net_connect = ConnectHandler(**my_device)

src_file = "testx.txt"
dest_file = "test-ktb.txt"
copy_cmd = f"copy flash:/{src_file} flash:/{dest_file}"
print(copy_cmd)

output = net_connect.send_command_timing(
    command_string=copy_cmd, strip_prompt=False, strip_command=False
)
if "Destination filename" in output:
    output += net_connect.send_command_timing(
        command_string="\n", strip_prompt=False, strip_command=False
    )
# If the destination file already exists, it will prompt you to 'confirm'.
if "Do you want to over write" in output:
    output += net_connect.send_command_timing(
        command_string="y", strip_prompt=False, strip_command=False
    )

print(output)
net_connect.disconnect()
