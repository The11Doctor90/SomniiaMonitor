#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.business.maskDataReader.bleReader import *
import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData

_PPG_SERVICE = "7DEF8321-7300-4EE6-8849-46FACE74CA2A"
_PPG_RX = "7DEF8321-7301-4EE6-8849-46FACE74CA2A"
_TIME, _HR, _SPO2, _PI, _BR = 0, 1, 2, 3, 4


class PpgReader:
    __client: bleak.BleakClient
    __ekg_param_data: PpgParameterData

    def __init__(self, client: bleak.BleakClient):
        self.__client = client
        self.__ekg_param_data = PpgParameterData()

    def read(self):
        data = read_data_by_client(self.__client, _PPG_RX)
        self.__ekg_param_data.set_time(data[_TIME])
        self.__ekg_param_data.set_heart_rate(data[_HR])
        self.__ekg_param_data.set_spo2(data[_SPO2])
        self.__ekg_param_data.set_perfusion_index(data[_PI])
        self.__ekg_param_data.set_breath_frequency(data[_BR])
        return self.__ekg_param_data

    def is_connected(self) -> bool:
        return self._client.is_connected

    def stop(self):
        close_connection(self.__client)