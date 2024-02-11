#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.business.maskDataReader.bleReader import *
import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData

_PPG_SERVICE = "7DEF8320-7300-4EE6-8849-46FACE74CA2A"
_PPG_RX = "7DEF8320-7301-4EE6-8849-46FACE74CA2A"


class PpgReader:
    _client: bleak.BleakClient

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        """formato di ritorno:
                time_stamp, hr, spo2, pi, br"""
        # TODO
        # dati generati random
        data = PpgParameterData()
        data.set_time(int(time.time()))
        data.set_heart_rate(randint(0,100))
        data.set_spo2(randint(0,100))
        data.set_perfusion_index(randint(0,100))
        data.set_breath_frequency(randint(0,100))
        return data
        # dati reali acquisiti
        #return read_data_by_client(self._client, _PPG_RX)

    def is_connected(self) -> bool:
        # TODO
        return True
        #return self._client.is_connected
