import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
}

with ConnectHandler(**my_device) as net_connect:

    filename = "cisco3-cfg-May-16-11-15-40.259-113"
    cmd = f"del flash:/{filename}"

    output = net_connect.send_command_timing(
        cmd, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "y", strip_prompt=False, strip_command=False
    )
    print(output)
