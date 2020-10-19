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

    filename = "cisco3-cfg-May-15-15-33-57.634-112"
    cmd = f"del flash:/{filename}"

    output = net_connect.send_command(
        cmd, expect_string=r"Delete filename", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string=r"confirm", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "y", expect_string=r"#", strip_prompt=False, strip_command=False
    )
    print(output)
