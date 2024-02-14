#  Copyright (c) Matteo Ferreri 2024.

import time
from random import randint
from datetime import datetime
from somniiaMonitor.model.inertial_parameter_data import InertialParameterData
from somniiaMonitor.business.maskDataReader.bleReader import *

_INERTIAL_SERVICE = "7DEF8322-7300-4EE6-8849-46FACE74CA2A"
_INERTIAL_RX = "7DEF8322-7301-4EE6-8849-46FACE74CA2A"
# _INERTIAL_RX = "7def8322-7301-4ee6-8849-46face74ca2a"

_TIME, _RMS, _ROLL, _PITCH, _YAW = 0, 1, 2, 3, 4


class InertialReader:
    __client: bleak.BleakClient
    __inertial_parameter_data: InertialParameterData

    def __init__(self, client: bleak.BleakClient):
        self.__client = client
        self.__inertial_parameter_data = InertialParameterData()

    def read(self):
        # """formato di ritorno:
        # time_stamp, rms, roll, pitch, yaw"""
        # # TODO
        # # dati generati random
        # data = InertialParameterData()
        # data.timestamp = int(time.time())
        # data.set_root_mean_square(randint(0, 100))
        # data.set_roll(randint(0, 100))
        # data.set_pitch(randint(0, 100))
        # data.set_yaw(randint(0, 100))

        # return data
        # dati reali acquisiti
        data = read_data_by_client(self.__client, _INERTIAL_RX)
        self.__inertial_parameter_data.set_time(data[_TIME])
        self.__inertial_parameter_data.set_root_mean_square(data[_RMS])
        self.__inertial_parameter_data.set_roll(data[_ROLL])
        self.__inertial_parameter_data.set_pitch(data[_PITCH])
        self.__inertial_parameter_data.set_yaw(data[_YAW])
        return self.__inertial_parameter_data

    def is_connected(self) -> bool:
        # TODO
        return True
        # return self._client.is_connected
