from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

import logging

logging.basicConfig(
    filename="netmiko_class7.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)


def netmiko_connect(device_name, device):
    """
    Successful connection returns: (True, connect_obj)

    Failed authentication returns: (False, None)
    """
    hostname = device["host"]
    port = device.get("port", 22)

    try:
        net_connect = ConnectHandler(**device)
        msg = f"Netmiko connection succesful to {hostname}:{port}"
        logger.info(msg)
        return (True, net_connect)
    except NetmikoAuthenticationException as e:
        msg = f"Authentication failure to: {device_name} {hostname}:{port}"
        logger.error(msg)
        return (False, None)
    except NetmikoTimeoutException as e:
        if "DNS failure" in str(e):
            msg = (
                f"Device {device_name} failed due to a DNS failure, hostname {hostname}"
            )
            logger.error(msg)
            return (False, None)
        elif "TCP connection to device failed" in str(e):
            msg = f"Netmiko was unable to reach the provided host and port: {hostname}:{port}"
            logger.error(msg)
            return (False, None)


if __name__ == "__main__":

    password = getpass()

    # DNS failure
    vmx1 = {
        "name": "vmx1",
        "device_type": "juniper_junos",
        "host": "invalid.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Invalid Port
    vmx2 = {
        "name": "vmx2",
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "port": 8022,
    }

    # Invalid password
    nxos1 = {
        "name": "nxos1",
        "device_type": "cisco_nxos",
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
    }

    # Valid - should connect
    nxos2 = {
        "name": "nxos2",
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Create a list containing the successful connections
    connections = []
    for device in (vmx1, vmx2, nxos1, nxos2):
        device_name = device.pop("name")
        conn_status, net_connect = netmiko_connect(device_name, device)
        if conn_status:
            connections.append(net_connect)

    for net_connect in connections:
        print("\nSuccessfully connected to device:")
        print("-" * 20)
        print(net_connect.find_prompt())
        print("\n\n")

