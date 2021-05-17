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
    interfaces = c.send_command('show ip int brief')
    print (interfaces)
    c.close()
except Exception as e:
    print(e)



