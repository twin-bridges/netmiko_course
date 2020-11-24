import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = (
    os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
)

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "test2.txt"
dest_file = "test2.txt"
direction = "get"
file_system = "flash:"

ssh_conn = ConnectHandler(**cisco3)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    # Overwrite the target file (if it already exists)
    overwrite_file=True,    # default "will not overwrite"
    # verify_file=True,     # default "will verify"
)
print(transfer_dict)
ssh_conn.disconnect()
