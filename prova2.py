#  Copyright (c) Matteo Ferreri 2023.
import string

import bluetooth as bluez
import select

# some constants
HEXMODE = 0
ASCIIMODE = 1
BOTHMODE = 2

searchThread = None
socket = None
services = None
connected = False
hexcount = 0
mode = BOTHMODE


def recieveSerial(data=None):
    if connected:
        r, _, _ = select.select([socket], [], [], 0)
        if r != []:
            s = socket.recv(1024)
    return True



def isCharPrintable(c):
    if (c in string.letters) or (c in string.digits) or (c in (string.punctuation + " ")):
        return True
    else:
        return False
    


def connectToDevice(data=None):
    """
        Connect the computer to a serial device
    """
    if connected:
        socket.close()
        connectButton.set_label("Connect")
        connected = False
        textBuffer.insert(textBuffer.get_end_iter(), "\n>> Disconnected from host\n")
        return

    socket = bluez.BluetoothSocket(bluez.RFCOMM)
    for s in services:
        if s["name"] == devicesList.get_active_text():
            try:
                textBuffer.insert(textBuffer.get_end_iter(), "\n>> Connecting to " + s["host"] + "... ")
                socket.connect((s["host"], s["port"]))
                connectButton.set_label("Disconnect")
                connected = True
                hexcount = 0
                textBuffer.insert(textBuffer.get_end_iter(), "[ OK ]\n")
            except Exception as e:
                print
                "Error, unable to connect ! ", e.message[1]
                connected = False
                connectButton.set_label("Connect")
                textBuffer.insert(textBuffer.get_end_iter(), "[FAIL]\n")
                    



def searchDevices():
        """
            Search for devices
        """
        searchButton.set_sensitive(False)
        print
        "Scanning for devices..."
        while devicesList.get_active() != -1:
            devicesList.remove_text(0)

        textBuffer.insert(textBuffer.get_end_iter(), ">> Searching Bluetooth serial ports... ")
        searchSpinner.start()
        searchSpinner.show()
        try:
            services = bluez.find_service(uuid=bluez.SERIAL_PORT_CLASS)
        except Exception as e:
            print
            "Error, unable to search devices :", e.message[1]
            return

        textBuffer.insert(textBuffer.get_end_iter(), "found " + str(len(services)) + "\n")
        for i in range(len(services)):
            print
            " -> Found", services[i]["name"], "at", services[i]["host"]
            textBuffer.insert(textBuffer.get_end_iter(),
                                   " -> " + services[i]["name"] +
                                   " (" + bluez.lookup_name(services[i]["host"], 3) + ") at " +
                                   services[i]["host"])
            devicesList.append_text(services[i]["name"])
            devicesList.set_active(0)

        searchSpinner.stop()
        searchSpinner.hide()
        searchButton.set_sensitive(True)
        if len(services) > 0:
        connectButton.set_sensitive(True)

