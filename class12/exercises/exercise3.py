import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    device = {
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    net_connect = ConnectHandler(**device)

    print("\n\nSend configuration commands to device:")
    cfg_commands = [
        "set system syslog archive size 110k files 3",
        "set system time-zone America/New_York",
    ]
    output = net_connect.send_config_set(cfg_commands)

    divider = "-" * 20
    print(f"\n{divider}\n{output}\n{divider}\n")

    print("Commit change...operation is slow")

    # Commit with a comment
    # output = net_connect.commit(comment="Configuration change using Netmiko (ktb)")

    print(f"\n{divider}\n{output}\n{divider}\n")
    print()

    commit_history = net_connect.send_command("show system commit")
    commit_history = commit_history.strip()
    commit_list = commit_history.splitlines()
    last_commit = commit_list[:2]
    last_commit = "\n".join(last_commit)
    print(last_commit)
