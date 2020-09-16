from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)
prompt = net_connect.find_prompt()
print(prompt)
net_connect.disconnect()
