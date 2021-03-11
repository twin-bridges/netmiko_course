import os
from getpass import getpass
from netmiko import ConnectHandler, redispatch


if __name__ == "__main__":

    debug = True
    arista4_internal_ip = "10.220.88.31"
    ssh_cmd = f"ssh -l pyclass {arista4_internal_ip}"

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Connect to Cisco3 using Netmiko
    print()
    print(f"Connecting to: {cisco3['host']}")
    net_connect = ConnectHandler(**cisco3)

    # Ensure connected to cisco3
    prompt = net_connect.find_prompt()
    if debug:
        print(f"\nCurrent prompt: {prompt}")
    print(f"Current class: {str(net_connect)}")

    # SSH to Arista4 from Cisco3
    print("\nSSH from Cisco3 to Arista4:")
    output = net_connect.send_command(
        ssh_cmd, expect_string=r"ssword", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        password, strip_prompt=False, strip_command=False
    )
    if debug:
        print(">>>>")
        print(output)
        print(">>>>")

    prompt = net_connect.find_prompt()

    # Use redispatch to switch the Netmiko class
    print("\nUse redispatch to switch the class.")
    redispatch(net_connect, device_type="arista_eos")
    print(f"Current class: {str(net_connect)}")
