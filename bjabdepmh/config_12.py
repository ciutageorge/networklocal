import paramiko
import time
from getpass import getpass


username = 'david'
password = 'cisco'

DEVICE_LIST = open ('/home/gns3/venv/python/bjabdepmh/09_devices')
for RTR in DEVICE_LIST:
    RTR = RTR.strip()
    print ('\n #### Connecting to the device ' + RTR + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(hostname=RTR,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    COMMANDS = open ('/home/gns3/venv/python/bjabdepmh/09_config')
    for LINES in COMMANDS:
        time.sleep(.5)
        DEVICE_ACCESS.send(str(LINES))

    time.sleep(1)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))

    SESSION.close