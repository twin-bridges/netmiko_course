from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "student1",
    "use_keys": True,
    "key_file": "~/.ssh/student_key",
    "disable_sha2_fix": True,
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
