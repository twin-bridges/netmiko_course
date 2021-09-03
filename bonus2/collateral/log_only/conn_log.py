import logging
from netmiko import ConnLogOnly
from devices import cisco3, cisco4, arista1, arista2

log_level = logging.INFO
log_file = "my_output.log"

for device in (cisco3, cisco4, arista1, arista2):
    net_connect = ConnLogOnly(log_file=log_file, log_level=log_level, **device)
    if net_connect:
        print(net_connect.find_prompt())
