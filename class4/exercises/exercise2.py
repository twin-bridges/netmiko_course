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
}

net_connect = ConnectHandler(**my_device)

src_file = "testx.txt"
dest_file = "test-ktb.txt"
copy_cmd = f"copy flash:/{src_file} flash:/{dest_file}"
print(copy_cmd)

output = net_connect.send_command(
    command_string=copy_cmd,
    expect_string=r"Destination filename",
    strip_prompt=False,
    strip_command=False,
)
output += net_connect.send_command(
    command_string="\n",
    expect_string=r"(confirm|\#)",
    strip_prompt=False,
    strip_command=False,
)
# If the destination file already exists, it will prompt you to 'confirm'.
if "confirm" in output:
    output += net_connect.send_command(
        command_string="y", expect_string=r"\#", strip_prompt=False, strip_command=False
    )

print(output)
net_connect.disconnect()
