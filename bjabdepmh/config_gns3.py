from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import requests

IP_LIST = open('/home/gns3/venv/python/bjabdepmh/09_devices1')
for IP in IP_LIST:
    print ('\n'+ IP.strip() + '  \n' )
    RTR = {
    'ip':   IP,
    'port': '3080',
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

    output = net_connect.send_config_from_file(config_file = '/home/gns3/venv/python/bjabdepmh/09_config1')
    print(output)

    print ('\n Saving the configuration \n')
    output = net_connect.save_config()
    print (output)

    output = net_connect.send_command('show ip int brief')
    print(output)
#NetmikoTimeoutExceptions​
#NetmikoCiscoAuthenticationException​
#NetmikoSSHException​