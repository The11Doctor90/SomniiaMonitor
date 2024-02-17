#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.business.maskDataReader.bleReader import *
from somniiaMonitor.model.sleep_stage_data import SleepStageData

_STAGING_SERVICE = "7DEF8322-7300-4EE6-8849-46FACE74CA2A"
_STAGING_RX = "7DEF8322-7301-4EE6-8849-46FACE74CA2A"

_TIME, _STAGE = 0, 1


class StagingReader:
    __client: bleak.BleakClient
    __sleep_stage_data: SleepStageData
    stages = ["stage 1", "stage 2", "stage 3", "stage 4"]

    def __init__(self, client: bleak.BleakClient):
        self.__client = client
        self.__sleep_stage_data = SleepStageData()

    def read(self):
        data = read_data_by_client(self.__client, _STAGING_RX)
        self.__sleep_stage_data.set_time(data[_TIME])
        self.__sleep_stage_data.set_stage(data[_STAGE])
        return self.__sleep_stage_data

    def is_connected(self) -> bool:
        return self._client.is_connected

    def stop(self):
        close_connection(self.__client)
