import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}
cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "cfg_name_servers.txt"
dest_file = "cfg_name_servers.txt"
direction = "put"
file_system = "flash:"

for device in (cisco3, cisco4):
    ssh_conn = ConnectHandler(**device)
    print("\n\n")
    print("-" * 20)
    print(f"\nTransferring configuration file: {device['host']}")
    file_exists, file_transferred, md5_verify = file_transfer(
        ssh_conn,
        source_file=source_file,
        dest_file=dest_file,
        file_system=file_system,
        direction=direction,
        overwrite_file=True,  # default "will not overwrite"
    )

    # Merge configuration change
    if file_exists and md5_verify:
        cmd = f"copy {file_system}/{ dest_file } system:running-config"
        output = ssh_conn.send_command_timing(
            cmd, strip_prompt=False, strip_command=False
        )
        # Device will prompt to verify: Destination filename [running-config]?
        if "Destination filename" in output and "running-config" in output:
            output += ssh_conn.send_command_timing(
                "\n", strip_prompt=False, strip_command=False
            )
        print(output)

    # Verify
    name_srv = ssh_conn.send_command("show run | inc name-server").strip()
    if len(name_srv.split()) != 4:
        # Checks there aren't extra name-servers
        print(f"\nThe name servers are not configured properly:\n>>> {name_srv}")
    if "8.8.8.8" in name_srv and "8.8.4.4" in name_srv:
        print("\nName servers are correct.")
    domain_name = ssh_conn.send_command("show run | inc domain")
    if "lasthop.io" in domain_name:
        print("\nDomain name is correct")
    ssh_conn.disconnect()
