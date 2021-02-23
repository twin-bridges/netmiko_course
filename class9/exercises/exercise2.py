import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "output.txt",
}


def redirect_output(ssh_conn, cmd):
    print("\n\nRedirecting 'show interfaces' output to flash:")
    output = ssh_conn.send_command_timing(cmd, strip_prompt=False, strip_command=False)

    # Command will prompt for confirmation if the file already exists
    if "confirm" in output:
        output += ssh_conn.send_command_timing(
            "y", strip_prompt=False, strip_command=False
        )
    return output


def more_file(ssh_conn, cmd):
    """Verify file was saved into flash:"""

    print("\nVerifying 'show interfaces' file exists on flash:")
    output_verify = ssh_conn.send_command(cmd)
    if "GigabitEthernet0/0/0" not in output_verify:
        raise ValueError(f"{cmd} does not contain expected value in output")
    return output_verify


if __name__ == "__main__":

    # Secure copy server must be enable on the device ('ip scp server enable')
    source_file = "show_interfaces_ktb.txt"
    dest_file = source_file
    direction = "get"
    file_system = "flash:"

    with ConnectHandler(**cisco3) as ssh_conn:

        # show interfaces | redirect flash:/show_interfaces_ktb.txt
        cmd = f"show interfaces | redirect {file_system}/{source_file}"
        redirect_output(ssh_conn, cmd)

        # more flash:/show_interfaces_ktb.txt
        cmd = f"more {file_system}/{source_file}"
        more_file(ssh_conn, cmd)

        # SCP Get the file
        print("\nRetrieving the file using SCP Get")
        transfer_dict = file_transfer(
            ssh_conn,
            source_file=source_file,
            dest_file=dest_file,
            file_system=file_system,
            direction=direction,
            # Overwrite the target file (if it already exists)
            overwrite_file=True,
        )
        file_exists = transfer_dict["file_exists"]
        md5_verify = transfer_dict["file_verified"]
        if file_exists and md5_verify:
            print("\n'show interfaces' file successfully transferred")
        else:
            raise ValueError("Error in transferring the file.")
