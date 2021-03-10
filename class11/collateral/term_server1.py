"""
Note: Students won't be able to run this code since the terminal server is not accessible.
"""
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = (
    os.getenv("TERM_SERVER_PASSWORD")
    if os.getenv("TERM_SERVER_PASSWORD")
    else getpass()
)

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
net_connect.disconnect()
