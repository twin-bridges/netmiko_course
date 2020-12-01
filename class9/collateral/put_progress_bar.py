import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer, progress_bar

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "testx.txt"
dest_file = "testx.txt"
direction = "put"
file_system = "flash:"

ssh_conn = ConnectHandler(**cisco3)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,  # default "will not overwrite"
    progress4=progress_bar,
)
ssh_conn.disconnect()
print(transfer_dict)
