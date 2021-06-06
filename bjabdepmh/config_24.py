from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import datetime

TNOW = datetime.datetime.now().replace(microsecond=0)
IP_LIST = open('/home/gns3/venv/python/bjabdepmh/09_devices')
for IP in IP_LIST:
    print ('\n'+ IP.strip() + '  \n' )
    RTR = {
    'ip':   IP,
    'username': 'david',
    'password': 'cisco',
    'device_type': 'cisco_ios',
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

    #output = net_connect.send_config_from_file(config_file = '/home/gns3/venv/python/bjabdepmh/09_config')
    #print(output)

    print ('\n Initiating config backup \n')
    output = net_connect.send_command('show run')
    #print (output)
    SAVE_FILE = open('ROUTER_' + IP + str(TNOW), 'w')
    SAVE_FILE.write(output)
    SAVE_FILE.close
    print ('\n Finishing config backup \n ')

   