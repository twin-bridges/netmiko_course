import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


def netmiko_exec(device):
    start_time = datetime.now()
    with ConnectHandler(**device) as net_connect:
        print(f"\n\nPrompt: {net_connect.find_prompt()}\n")
    end_time = datetime.now()
    return end_time - start_time


# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
base_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Case1 fast_cli=True and no global_delay_factor (defaults)
case1 = base_device.copy()
exec_time = netmiko_exec(case1)
print(f"Case1 Execution Time (fast_cli=True/no global_delay_factor): {exec_time}")

# Case2 fast_cli=False and no global_delay_factor
case2 = base_device.copy()
case2["fast_cli"] = False
exec_time = netmiko_exec(case2)
print(f"Case2 Execution Time (fast_cli=False/no global_delay_factor): {exec_time}")

# Case3 fast_cli=False and global_delay_factor=2
case3 = base_device.copy()
case3["fast_cli"] = False
case3["global_delay_factor"] = 2
exec_time = netmiko_exec(case3)
print(f"Case3 Execution Time (fast_cli=False/global_delay_factor=2): {exec_time}")

# Case4 fast_cli=False and global_delay_factor=4
case4 = base_device.copy()
case4["fast_cli"] = False
case4["global_delay_factor"] = 4
exec_time = netmiko_exec(case4)
print(f"Case4 Execution Time (fast_cli=False/global_delay_factor=4): {exec_time}")
