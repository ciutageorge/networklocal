from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.122.72', 'david', 'cisco')
device.open()

device.load_replace_candidate(filename='/home/gns3/venv/python/bjabdepmh/sw1_cisco_backup')
#device.load_merge_candidate(filename='/home/gns3/venv/python/bjabdepmh/29_cisco_route')
print (device.compare_config())

if len(device.compare_config()) > 0:
    choice = input("\nWould you like to Replace the configuration? [y/N]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()
        choice = input("\nWould you like to Rollback the configuration? [y/N]: ")
        if choice == 'y':
            print('Committing ...')
            device.rollback()
    else:
        print('Discarding ...')
        device.discard_config()
else:
    print ('No difference')
#close the session with the device
device.close()
print('Done.')