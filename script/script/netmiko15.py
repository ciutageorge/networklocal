#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.76',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.77',
    'username': 'david',
    'password': 'cisco',
}

with open('/home/gns3/venv/python/script/iosv_l2_config') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output) 

with open('/home/gns3/venv/python/script/iosv_l2_config1') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output) 