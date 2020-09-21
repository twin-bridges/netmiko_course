import os
import time
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

time.sleep(4)

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    session_log="cisco3.out",
)
print(net_connect.find_prompt())
output = net_connect.send_command("show ip int brief")
print(output)
net_connect.disconnect()
