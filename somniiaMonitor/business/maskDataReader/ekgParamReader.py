#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.ekg_parameter_data import EkgParameterData

from somniiaMonitor.business.maskDataReader.bleReader import *

_EKG_PARAM_SERVICE = "7DEF8319-7300-4EE6-8849-46FACE74CA2A"
_EKG_PARAM_RX = "7DEF8319-7301-4EE6-8849-46FACE74CA2A"
_TIME, _HR, _HRV, _RR = 0, 1, 2, 3


class EkgParamReader:
    __client: bleak.BleakClient
    __ekg_param_data: EkgParameterData

    def __init__(self, client: bleak.BleakClient):
        self.__client = client
        self.__ekg_param_data = EkgParameterData()

    def read(self):
        data = read_data_by_client(self.__client, _EKG_PARAM_RX)
        self.__ekg_param_data.set_time(data[_TIME])
        self.__ekg_param_data.set_heart_rate(data[_HR])
        self.__ekg_param_data.set_heart_rate_variability(data[_HRV])
        self.__ekg_param_data.set_rr_interval(data[_RR])
        return self.__ekg_param_data

    def is_connected(self) -> bool:
        return self._client.is_connected

    def stop(self):
        close_connection(self.__client)
