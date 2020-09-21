import os
from getpass import getpass
from netmiko import ConnectHandler


# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

net_connect = ConnectHandler(
    device_type="cisco_ios",
    # device_type="invalid",
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
)
print(net_connect.find_prompt())
