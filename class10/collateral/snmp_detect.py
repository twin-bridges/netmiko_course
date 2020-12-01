import os
from getpass import getpass
from netmiko.snmp_autodetect import SNMPDetect

snmp_key = os.getenv("SNMP_COMMUNITY")
if not snmp_key:
    snmp_key = getpass("Enter SNMP community: ")

my_snmp = SNMPDetect(
    "cisco1.lasthop.io",
    snmp_version="v3",
    user="pysnmp",
    auth_key=snmp_key,
    encrypt_key=snmp_key,
    auth_proto="sha",
    encrypt_proto="aes128",
)

device_type = my_snmp.autodetect()
print(f"\n{device_type}\n")
