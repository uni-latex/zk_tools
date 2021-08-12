#!/usr/bin/python

from zk import ZK, const
import datetime
import time

def displayMessage(message):
    messageTime = datetime.datetime.now().strftime('%d %b %Y, %H:%M:%S')
    message =  "[ {} ] {}".format(messageTime, message)
    print(message)

devices = {
    "Pabrik B"                      : "192.168.10.20",      #   OK
    "Pabrik B Sortasi"              : "192.168.10.21",      #   OK
    "Kantor Utama"                  : "192.168.10.208",     #   OK
    "Pabrik A Sortasi"              : "192.168.11.20",      #   CANT REACH
    "Pabrik C"                      : "192.168.12.20",      #   OK
    "Pabrik C Sortasi"              : "192.168.12.21",      #   OK
    "Pabrik D"                      : "192.168.14.21",      #   OK
    "Pabrik D Sortasi"              : "192.168.14.22",      #   OK
    "Pabrik E 1"                    : "192.168.15.20",      #   OK
    "Pabrik E 2"                    : "192.168.15.21",      #   OK
    "Pabrik E Sortasi"              : "192.168.15.22",      #   OK
    "Pabrik F"                      : "192.168.16.21",      #   OK
    "F KHL /  KHT"                  : "172.16.56.6",        #   OK
    "Parkiran Pabrik C"             : "172.16.56.7",        #   OK
    "H Proyek"                      : "172.16.56.8",        #   OK
    "I Pabrik E"                    : "172.16.56.9",        #   OK
    
}

test = False

for device in devices:
    conn = None
    displayMessage('Device ' + device + ' on IP ' + devices[device])
    displayMessage('Connecting to device...')
    try:
        zk = ZK(devices[device])
        conn = zk.connect()
        if test:
            displayMessage("Device Name: " + conn.get_device_name())
            displayMessage("Platform: " + conn.get_platform())
            displayMessage("Firmware: " + conn.get_firmware_version())
            displayMessage("Serial Number: " + conn.get_serialnumber())
        else:
            displayMessage('Restarting device...')
            conn.restart()
            displayMessage('Done restart')
    except Exception as e:
        displayMessage('*** ERROR status: ' + str(e) + ' ***')
    