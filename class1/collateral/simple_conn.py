from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
)
prompt = net_connect.find_prompt()
print(prompt)
