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

    hosts = [
        "cisco3.lasthop.io",
        "cisco4.lasthop.io",
        "nxos1.lasthop.io",
        "nxos2.lasthop.io",
        "vmx1.lasthop.io",
        "vmx2.lasthop.io",
    ]

    pool = ThreadPoolExecutor(20)

    future_list = []
    for hostname in hosts:
        future = pool.submit(find_device_type, hostname)
        future_list.append(future)

    # Display the results
    for future in as_completed(future_list):
        hostname, device_type = future.result()
        print(f"{hostname} --> {device_type}")
