
from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "invalid.lasthop.io",
    "username": "testuser",
    "use_keys": True,
    "key_file": "~/.ssh/test_rsa"
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
