import os
import time
from netmiko import ConnectHandler, redispatch
from getpass import getpass

# Code so automated tests will run properly
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

net_connect.write_channel("\r")
time.sleep(0.5)
net_connect.write_channel("\r")
time.sleep(0.5)
output = net_connect.read_channel()
print(output)

# Now login to the end device
try:
    if "sername" in output:
        # Code so automated tests will run properly
        end_device_pwd = (
            os.getenv("NETMIKO_PASSWORD")
            if os.getenv("NETMIKO_PASSWORD")
            else getpass()
        )

        net_connect.username = "pyclass"
        net_connect.password = end_device_pwd
        net_connect.secret = end_device_pwd
        net_connect.std_login()
        net_connect.set_base_prompt()
        print(net_connect.find_prompt())

        # We are fully logged into the end device; we now must switch the Netmiko class
        redispatch(net_connect, device_type="cisco_ios_telnet")

        print(net_connect)
        print(net_connect.send_command("show ip int brief"))
        net_connect.enable()
        print(net_connect.send_config_set("logging buffered 30000"))
        net_connect.write_channel("exit\r")
        time.sleep(0.5)
    else:
        raise ValueError("Username prompt not found")
finally:
    net_connect.disconnect()
