import os
from netmiko import ConnectHandler, NetmikoTimeoutException
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    # "fast_cli": False,
    "session_log": "nxos1.out",
}

with ConnectHandler(**nxos1) as net_connect:

    print("\n\nChanging the terminal width...")
    output = net_connect.send_command("terminal width 80")

    print("\nSetting the hostname to a very long value...")
    output = net_connect.send_config_set("hostname verylonghostnamefornxos")

    # Will fail
    print("\nTesting long command that should now fail due to line-wrap issues")
    try:
        cmd = "show ip interface brief vrf management | include management"
        output = net_connect.send_command(cmd)
        print(f"\n{output}\n")
    except NetmikoTimeoutException:
        print("...long command failed with an exception")

    # Try again but disable cmd_verify
    banner = "-" * 12
    print("\n\nTrying again with cmd_verify disabled...should work:")
    output = net_connect.send_command(cmd, cmd_verify=False)
    print(f"{banner}\n{output}\n{banner}")

    # Try again but disable global_cmd_verify
    net_connect.global_cmd_verify = False
    print("Trying again with global_cmd_verify disabled...should work:")
    output = net_connect.send_command(cmd)
    print(f"{banner}\n{output}\n{banner}")

    print("\n\nRestoring hostname to original value...\n")
    output = net_connect.send_config_set("hostname nxos1")
