import os
import yaml
from getpass import getpass
from netmiko import SSHDetect
from concurrent.futures import ThreadPoolExecutor, as_completed


# Code so automated tests will run properly
PASSWORD = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


def find_device_type(hostname):

    base_device = {
        "device_type": "autodetect",
        "username": "pyclass",
        "password": PASSWORD,
    }

    device = base_device.copy()
    device["host"] = hostname
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    return (hostname, best_match)


if __name__ == "__main__":

    hosts_file = "my_hosts.txt"
    with open(hosts_file) as f:
        hosts = f.readlines()

    pool = ThreadPoolExecutor(20)
    future_list = []
    for hostname in hosts:
        hostname = hostname.strip()
        future = pool.submit(find_device_type, hostname)
        future_list.append(future)

    # Display the results
    my_devices = {}
    print()
    for future in as_completed(future_list):
        hostname, device_type = future.result()
        print(f"{hostname} -> {device_type}")
        name = hostname.split(".")[0]
        my_devices[name] = {}
        my_devices[name]["hostname"] = hostname
        my_devices[name]["device_type"] = device_type
    print()

    # Write external YAML file
    print("\nCreating devices.yaml file\n\n")
    with open(r"devices.yaml", "w") as f:
        yaml.dump(my_devices, f)
