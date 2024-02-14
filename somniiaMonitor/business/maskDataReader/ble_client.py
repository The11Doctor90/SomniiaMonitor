#  Copyright (c) Matteo Ferreri 2024.
import bleak

from somniiaMonitor.business.maskDataReader import bleReader


class BleClient:
    __client: bleak.BleakClient

    def __init__(self, mac_address: str):
        self.__client = bleReader.create_client_by_address(mac_address)
        bleReader.connect_to_device(self.__client)

    def get_client(self) -> bleak.BleakClient:
        return self.__client

    def close_connection(self):
        bleReader.close_connection(self.__client)
