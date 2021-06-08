from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import datetime
import schedule

def BACKUP():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    IP_LIST = open('/home/gns3/venv/python/bjabdepmh/09_devices')
    for IP in IP_LIST:
        #print ('\n  '+ IP.strip() + '  \n' )
        RTR = {
        'ip':   IP,
        'username': 'david',
        'password': 'cisco',
        'device_type': 'cisco_ios',
        }
        print ('\n #### Connecting to the device ' + IP.strip() + '#### \n')
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

        print ('Initiating cofig backup at ' + str(TNOW))
        output = net_connect.send_command('show run')

        SAVE_FILE = open("RTR_" + IP +'_'+ str(TNOW), 'w')
        SAVE_FILE.write(output)
        SAVE_FILE.close
        print ('Finished config backup')
schedule.every().minute.at(":00").do(BACKUP)
while True:
    schedule.run_pending()
    time.sleep(1)