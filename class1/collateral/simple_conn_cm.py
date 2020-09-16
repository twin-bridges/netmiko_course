from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
}

with ConnectHandler(**my_device) as net_connect:
    prompt = net_connect.find_prompt()
    print(prompt)
