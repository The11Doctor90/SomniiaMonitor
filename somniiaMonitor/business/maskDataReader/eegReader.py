#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.eeg_signal_data import EegSignalData

from somniiaMonitor.business.maskDataReader.bleReader import *

_EEG_SERVICE = "7DEF8319-7300-4EE6-8849-46FACE74CA2A"
_EEG_RX = "7DEF8319-7301-4EE6-8849-46FACE74CA2A"


class EegReader:
    _client: bleak.BleakClient

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        """formato di ritorno:
        time_stamp, ch_1, ch_2, ch_3"""
        # TODO
        # dati generati random
        data = EegSignalData()
        data.set_time(int(time.time()))
        data.set_first_channel(randint(0, 100))
        data.set_second_channel(randint(0, 100))
        data.set_third_channel(randint(0, 100))
        return data
        # dati reali acquisiti
        # return read_data_by_client(self._client, _EEG_RX)

    def is_connected(self) -> bool:
        # TODO
        return True
        # return self._client.is_connected
