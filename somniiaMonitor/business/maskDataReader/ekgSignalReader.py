#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.business.maskDataReader.bleReader import *
from somniiaMonitor.model.ekg_signal_data import EkgSignalData

_EKG_SIGNAL_SERVICE = "7DEF8318-7300-4EE6-8849-46FACE74CA2A"
_EKG_SIGNAL_RX = "7DEF8318-7301-4EE6-8849-46FACE74CA2A"

_TIME, _SIGNAL = 0, 1


class EkgSignalReader:
    __client: bleak.BleakClient
    __ekg_signal_data: EkgSignalData

    def __init__(self, client: bleak.BleakClient):
        self.__client = client
        self.__ekg_signal_data = EkgSignalData()

    def read(self):
        data = read_data_by_client(self.__client, _EKG_SIGNAL_RX)
        self.__ekg_signal_data.set_time(data[_TIME])
        self.__ekg_signal_data.set_signal(data[_SIGNAL])
        return self.__ekg_signal_data

    def is_connected(self) -> bool:
        # TODO
        return True
        # return self._client.is_connected

    def stop(self):
        close_connection(self.__client)
