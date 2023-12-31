import socket
import bluetooth

# addr = 'B8:86:87:0F:5E:EA'
addr = '12:6C:14:39:27:E6'
channel = 1


# def main():
#     server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#     # server.bind(("00:00:00:00:00:00", 4))
#     server.bind((addr, channel))
#     server.listen(1)
#
#     print("In attesa di connessioni Bluetooth...")
#     client, address = server.accept()
#
#     print(f"Connesso a: {address}")
#
#
#     try:
#         while True:
#             data = client.recv(1024)
#             if not data:
#                 break
#             print(f"Message: {data.decode('utf-8')}")
#     except OSError as e:
#         pass
#
#     client.close()
#     server.close()


# def main():
#     nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
#     print("Found {} devices.".format(len(nearby_devices)))
#
#     for addr, name, device_class in nearby_devices:
#         print("  {} - {} - {}".format(addr, name, device_class))

def main():
    soc = bluetooth.BluetoothSocket()
    soc.connect((addr, channel))

    while True:
        data = soc.recv(1024)
        data = str(data, encoding='ascii')
        print(data)

    soc.close()



if __name__ == '__main__':
    main()

