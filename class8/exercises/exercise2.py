import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from getpass import getpass

# Store certain functions in another module so the can be used across multiple exercises.
from utilities import load_devices, ssh_conn


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_devices = load_devices()
    device_list = my_devices["all"]
    pool = ProcessPoolExecutor(20)

    cmd_dict = {"cisco_nxos": "show ip arp vrf management", "juniper_junos": "show arp"}

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        platform = device_dict["device_type"]

        # If cmd is not in cmd_dict, default to "show ip arp"
        cmd = cmd_dict.get(platform, "show ip arp")
        future = pool.submit(
            ssh_conn, device_name=device_name, device_dict=device_dict, cmd=cmd
        )
        future_list.append(future)

    # Display the results
    for future in as_completed(future_list):
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()
