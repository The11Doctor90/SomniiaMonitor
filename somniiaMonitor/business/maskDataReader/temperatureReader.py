#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.temperature_data import TemperatureData
from somniiaMonitor.business.maskDataReader.bleReader import *

_TEMPERATURE_SERVICE = "7DEF8324-7300-4EE6-8849-46FACE74CA2A"
_TEMPERATURE_RX = "7DEF8324-7301-4EE6-8849-46FACE74CA2A"
_TIME, _TEMP = 0, 1


class TemperatureReader:
    __client: bleak.BleakClient
    __temperature_data: TemperatureData

    def __init__(self, client: bleak.BleakClient):
        self.__client = client
        self.__temperature_data = TemperatureData()

    def read(self):
        data = read_data_by_client(self.__client, _TEMPERATURE_RX)
        self.__temperature_data.set_time(data[_TIME])
        self.__temperature_data.set_temperature(data[_TEMP])
        return self.__temperature_data

    def is_connected(self) -> bool:
        # TODO
        return True
        # return self._client.is_connected

    def stop(self):
        close_connection(self.__client)
