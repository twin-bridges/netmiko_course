from netmiko import ConnectHandler

base_device = {
    "device_type": "cisco_ios",
    "username": "student1",
    "password": "cisco123",
    "use_keys": True,
    "key_file": "~/.ssh/student_key",
}

cisco3 = base_device.copy()
cisco3["host"] = "cisco3.lasthop.io"
cisco4 = base_device.copy()
cisco4["host"] = "cisco4.lasthop.io"

for device in (cisco3, cisco4):
    with ConnectHandler(**device) as net_connect:
        print()
        print(net_connect.find_prompt())
        print("-" * 12)
        output = net_connect.send_command("show ip arp")
        print(f"{output}\n")
