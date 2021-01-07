import time
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

term_server = {
    "device_type": "generic_termserver_telnet",
    "host": "184.105.247.69",
    "username": "admin",
    "password": password,
    "session_log": "term_server.out",
}

net_connect = ConnectHandler(**term_server)
net_connect.std_login()
print(net_connect.find_prompt())

net_connect.write_channel("cisco3\r")
time.sleep(1)
output = net_connect.read_channel()
print(output)

# Send an extra enter
net_connect.write_channel("\r")
time.sleep(1)
output = net_connect.read_channel()
print(output)

net_connect.disconnect()
