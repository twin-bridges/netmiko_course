import os
import yaml
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def ssh_conn(device, cmd=None):
    net_connect = ConnectHandler(**device)
    if cmd is None:
        return net_connect.find_prompt()
    else:
        output = net_connect.send_command(cmd)
        return output


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_devices = load_devices()
    arista_list = my_devices["arista"]
    cisco_list = my_devices["cisco"]
    nxos_list = my_devices["nxos"]
    device_list = arista_list + cisco_list + nxos_list

    start_time = datetime.now()
    max_threads = 4

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        # future = pool.submit(ssh_conn, device_dict, "show ip arp")
        future = pool.submit(ssh_conn, device=device_dict, cmd="show ip arp")
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    for future in future_list:
        print("Result: " + future.result())

    end_time = datetime.now()
    print(end_time - start_time)
