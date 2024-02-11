#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.inertial_parameter_data import InertialParameterData
from somniiaMonitor.business.maskDataReader.bleReader import *

_INERTIAL_SERVICE = "7DEF8322-7300-4EE6-8849-46FACE74CA2A"
_INERTIAL_RX = "7DEF8322-7301-4EE6-8849-46FACE74CA2A"


class InertialReader:
    _client: bleak.BleakClient

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        """formato di ritorno:
        time_stamp, rms, roll, pitch, yaw"""
        # TODO
        # dati generati random
        data = InertialParameterData()
        data.timestamp = int(time.time())
        data.set_root_mean_square(randint(0, 100))
        data.set_roll(randint(0, 100))
        data.set_pitch(randint(0, 100))
        data.set_yaw(randint(0, 100))

        return data
        # dati reali acquisiti
        #return read_data_by_client(self._client, _INERTIAL_RX)

    def is_connected(self) -> bool:
        # TODO
        return True
        #return self._client.is_connected
