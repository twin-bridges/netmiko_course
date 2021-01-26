"""
no global_delay_factor and fast_cli=True 3.7 seconds
no global_delay_factor and fast_cli=False 4.4 seconds
global_delay_factor=2 and fast_cli=False 7.1 seconds
global_delay_factor=4 and fast_cli=False 12.8 seconds

"""
import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Case1 fast_cli=True and no global_delay_factor
my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    # "fast_cli": True,     This is the default value
    # "global_delay_factor": 1, This is the default value
    
}

start_time = datetime.now()
with ConnectHandler(**my_device) as net_connect:
    print(net_connect.find_prompt())
end_time = datetime.now()
exec_time = end_time - start_time
print(f"Case1 Execution Time (fast_cli=True/no global_delay_factor): {exec_time}")
