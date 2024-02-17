#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.eeg_signal_data import EegSignalData

from somniiaMonitor.business.maskDataReader.bleReader import *

_EEG_SERVICE = "7DEF8320-7300-4EE6-8849-46FACE74CA2A"
_EEG_RX = "7DEF8320-7301-4EE6-8849-46FACE74CA2A"

_TIME, _FIRST, _SECOND, _THIRD = 0, 1, 2, 3


class EegReader:
    __client: bleak.BleakClient
    __eeg_signal_data: EegSignalData

    def __init__(self, client: bleak.BleakClient):
        self.__client = client
        self.__eeg_signal_data = EegSignalData()

    def read(self):
        data = read_data_by_client(self.__client, _EEG_RX)
        self.__eeg_signal_data.set_time(data[_TIME])
        self.__eeg_signal_data.set_first_channel(data[_FIRST])
        self.__eeg_signal_data.set_second_channel(data[_SECOND])
        self.__eeg_signal_data.set_third_channel(data[_THIRD])
        return self.__eeg_signal_data

    def is_connected(self) -> bool:
        return self._client.is_connected

    def stop(self):
        close_connection(self.__client)
