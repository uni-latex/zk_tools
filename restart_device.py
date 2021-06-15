#!/usr/bin/python

from zk import ZK, const

devices = {
    "Pabrik B"                      : "192.168.10.20",      #   OK
    "Pabrik B Sortasi"              : "192.168.10.21",      #   OK
    "Kantor Utama"                  : "192.168.10.208",     #   OK
    "Pabrik C"                      : "192.168.12.20",      #   OK
    "Pabrik C Sortasi"              : "192.168.12.21",      #   OK
    "Pabrik D"                      : "192.168.14.21",      #   OK
    "Pabrik D Sortasi"              : "192.168.14.22",      #   OK
    "Pabrik E 1"                    : "192.168.15.20",      #   OK
    "Pabrik E 2"                    : "192.168.15.21",      #   OK
    "Pabrik E Sortasi"              : "192.168.15.22",      #   OK
    "F KHL /  KHT"                  : "172.16.56.6",        #   OK
    "Parkiran Pabrik C"             : "172.16.56.7",        #   OK
    "H Proyek"                      : "172.16.56.8",        #   OK
    "I Pabrik E"                    : "172.16.56.9",        #   OK
    "Pabrik A Sortasi"              : "172.16.56.10",       #   CANT REACH
}

test = False

for device in devices:
    conn = None
    print('Device ' + device + ' on IP ' + devices[device])
    print('Connecting to device...')
    try:
        zk = ZK(devices[device])
        conn = zk.connect()
        if test:
            print("Device Name: " + conn.get_device_name())
            print("Platform: " + conn.get_platform())
            print("Firmware: " + conn.get_firmware_version())
            print("Serial Number: " + conn.get_serialnumber())
        else:
            print('Restarting device...')
            conn.restart()
            print('Done restart')
    except Exception as e:
        print('Restart status: ' + str(e))
    