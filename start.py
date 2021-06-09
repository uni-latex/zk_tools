from zk import ZK, const

devices = {
    "Kantor Utama" : "192.168.10.208",
}

for device in devices:
    conn = None
    print('Device ' + device + ' on IP ' + devices[device])
    print('Connecting to device...')
    try:
        zk = ZK(devices[device])
        conn = zk.connect()
        print('Restarting device...')
        conn.restart()
    except Exception as e:
        print('Restart status: ' + str(e))
    print('Done restart')
    
# conn = None
# zk = ZK('192.168.10.208')

# try:
#     print('Connecting to device...')
#     conn = zk.connect()

#     # print(conn.get_firmware_version())              #       Ver 6.60 Jun  9 2017
#     # print(conn.get_serialnumber())                  #       OID7040597040501719
#     # print(conn.get_platform())                      #       JZ4725_TFT
#     # print(conn.get_device_name())                   #       MP 340
#     # print(conn.get_face_version())                  #       None
#     # print(conn.get_fp_version())                    #       10
#     # print(conn.get_extend_fmt())                    #       0
#     # print(conn.get_user_extend_fmt())               #       1
#     # print(conn.get_face_fun_on())                   #       None
#     # print(conn.get_compat_old_firmware())           #       None
#     # print(conn.get_network_params())                #       {'ip': '192.168.10.20', 'mask': '255.255.255.0', 'gateway': '192.168.10.254'}
#     # print(conn.get_mac())                           #       00:17:61:10:9E:D1
#     # print(conn.get_pin_width())                     #       9

#     # conn.read_sizes()
#     # print(conn)                                     #       ZK tcp://192.168.10.20:4370 users[72]:280/1000 fingers:1/1000, records:959/80000 faces:0/0
#     # print(conn.users)                               #       280
#     # print(conn.fingers)                             #       1
#     # print(conn.records)                             #       959
#     # print(conn.users_cap)                           #       1000
#     # print(conn.fingers_cap)                         #       1000

#     # users = conn.get_users()
#     # print(users)                    
    
#     print('Restarting device...')
#     conn.restart()
#     # conn.poweroff()

#     # print('Disabling device...')
#     # conn.disable_device()

#     # print('Enabling device...')
#     # conn.enable_device()
# except Exception as e:
#     print("Process terminate : {}".format(e))
# finally:
#     if conn:
#         print('Disconnecting...')
#         conn.disconnect()