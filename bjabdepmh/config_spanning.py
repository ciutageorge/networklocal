#!/usr/bin/env python
import os
from netmiko import ConnectHandler
import json

# Conectare la switch SW1
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'david',
    'password': 'cisco',
}

try:
    c = ConnectHandler(**iosv_l2)
    c.enable()
    stps = c.send_command('show spanning-tree', use_textfsm=True)
    print (json.dumps(stps, indent=2))
    for stp in stps:
        print('')
        print (f"{stp['interface']}.{stp['vlan_id']} are rolul de {stp['role']}")
    c.close()
except Exception as e:
    print(e)



