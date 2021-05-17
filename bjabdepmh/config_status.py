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
    interfaces = c.send_command('show interface status', use_textfsm=True)
    print (json.dumps(interfaces, indent=2))
    for interface in interfaces:
        if interface['status'] == 'connected':
           print (f"g {interface['port']} din vlanul {interface['vlan']} este conectat!")
    c.close()
except Exception as e:
    print(e)



