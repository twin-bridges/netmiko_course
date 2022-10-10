from netmiko import ConnectHandler

# Key file is now encrypted
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "testuser",
    # Just make the password be the key passphrase
    "password": "cisco123",
    "use_keys": True,
    "key_file": "~/.ssh/test_rsa_encr",
    "disable_sha2_fix": True,
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
