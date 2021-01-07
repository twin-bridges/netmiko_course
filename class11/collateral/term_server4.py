import os
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

# Try to find the
net_connect.write_channel("\r")
time.sleep(0.5)
net_connect.write_channel("\r")
time.sleep(0.5)
output = net_connect.read_channel()
print(output)

# Now login to the end device
if "sername" in output:

    # Code so automated tests will run properly
    end_device_pwd = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    net_connect.username = "pyclass"
    net_connect.password = end_device_pwd
    net_connect.std_login()
    print(net_connect.find_prompt())

net_connect.disconnect()
