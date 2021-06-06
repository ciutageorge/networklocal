from netmiko import ConnectHandler
from getpass import getpass
from operator import itemgetter
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


IP_LIST = open('/home/gns3/venv/python/bjabdepmh/09_devices1')
for IP in IP_LIST:
    RTR = {
    'device_type': 'cisco_ios',
    'ip':   IP,
    'username': 'david',
    'password': 'cisco',
    }
    print ('\n ##### Connecting to the device ' + IP.strip() + '##### \n')
    try:
        net_connect = ConnectHandler(**RTR)
    except NetMikoTimeoutException:
        print ('Device not reachable.')
        continue
    except AuthenticationException:
        print ('Authentication Failure.')
        continue
    except SSHException:
        print ('Make sure SSH is enabled in device.')
        continue
    print ('\nOUTPUT FOR DEVICE \n')    
    output = net_connect.send_command('show ip int brie', use_textfsm=True)
    print(output)

    print ('\nOUTPUT USING FOR LOOP AND IF \n')
    devlist = []
for i in output:
    if i['status'] == 'up':
        devlist.append(i['intf'])
print(devlist)

print ('\nOUTPUT USING LIST COMPREHENSION \n')

print ([i['intf'] for i in output if i['status'] == 'up'])

print('\n \n')

print ('\nList of interfaces which are UP \n#################')
statusup =[i['intf'] for i in output if i['status'] == 'up']
for ifaceup in statusup:
    print (ifaceup)

print ('\nList of interfaces which are DOWN \n###############')
statusother =[i for i in output if i['status'] != 'up']
for ifaceother in statusother:
    print (ifaceother['intf'] + ' ' + ifaceother['status']  )

