#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.temperature_data import TemperatureData
from somniiaMonitor.business.maskDataReader.bleReader import *

_TEMPERATURE_SERVICE = "7DEF8323-7300-4EE6-8849-46FACE74CA2A"
_TEMPERATURE_RX = "7DEF8323-7301-4EE6-8849-46FACE74CA2A"


class TemperatureReader:
    _client: bleak.BleakClient

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        """formato di ritorno:
                        time_stamp, temperature"""
        # TODO
        # dati generati random
        data = TemperatureData()
        data.set_time(int(time.time()))
        data.set_temperature(randint(0, 100))
        return data
        # dati reali acquisiti
        #return read_data_by_client(self._client, _TEMPERATURE_RX)

    def is_connected(self) -> bool:
        # TODO
        return True
        #return self._client.is_connected
