from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()
time.sleep(5)

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    session_log="cisco3.out",
)
prompt = net_connect.find_prompt()
print(prompt)
output = net_connect.send_command("show ip int brief")
print(output)
net_connect.disconnect()
