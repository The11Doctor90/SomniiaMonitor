#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.business.maskDataReader.bleReader import *
import time
from random import choice
from datetime import datetime
from somniiaMonitor.model.sleep_stage_data import SleepStageData

_STAGING_SERVICE = "7DEF8321-7300-4EE6-8849-46FACE74CA2A"
_STAGING_RX = "7DEF8321-7301-4EE6-8849-46FACE74CA2A"


class StagingReader:
    _client: bleak.BleakClient
    stages = ["stage 1", "stage 2", "stage 3", "stage 4"]

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        """formato di ritorno:
                time_stamp, stage"""
        # TODO
        # dati generati random
        data = SleepStageData()
        data.set_time(int(time.time()))
        data.set_stage(choice(self.stages))
        return data
        # dati reali acquisiti
        #return read_data_by_client(self._client, _STAGING_RX)

    def is_connected(self) -> bool:
        # TODO
        return True
        #return self._client.is_connected
