#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.ekg_parameter_data import EkgParameterData

from somniiaMonitor.business.maskDataReader.bleReader import *

_EKG_SERVICE = "7DEF8318-7300-4EE6-8849-46FACE74CA2A"
_EKG_RX = "7DEF8318-7301-4EE6-8849-46FACE74CA2A"


class EkgReader:
    _client: bleak.BleakClient

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        """formato di ritorno:
                time_stamp, hr, hrv, rr_interval"""
        # TODO
        # dati generati random
        data = EkgParameterData()
        data.set_time(int(time.time()))
        data.set_heart_rate(randint(0,100))
        data.set_heart_rate_variability(randint(0,100))
        data.set_rr_interval(randint(0,100))
        return data
        # dati reali acquisiti
        #return read_data_by_client(self._client, _EKG_RX)

    def is_connected(self) -> bool:
        # TODO
        return True
        #return self._client.is_connected
