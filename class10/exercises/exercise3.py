import os
import time
from getpass import getpass
from netmiko import ConnectHandler

def read_device(net_connect, sleep=1):
    """Sleep and read channel."""
    time.sleep(sleep)
    output = net_connect.read_channel()
    print(output)
    return output


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

    my_device = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "output.txt",
    }
    
    with ConnectHandler(**my_device) as net_connect:
    
        net_connect.write_channel("show ip int brief\n")
        read_device(net_connect, sleep=1)
    
        cmd = "telnet 10.220.88.22\n"
        net_connect.write_channel(cmd)
        output = read_device(net_connect, sleep=1)

        if "sername" in output:
            net_connect.write_channel(my_device["username"] + "\n")
        output = read_device(net_connect, sleep=1)
    
        if "ssword" in output:
            net_connect.write_channel(password + "\n")
        read_device(net_connect, sleep=1)
    
        net_connect.write_channel("exit\n")
        read_device(net_connect, sleep=1)
