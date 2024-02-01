#  Copyright (c) Matteo Ferreri 2024.

from bleReader import *

_INERTIAL_SERVICE = "7DEF8322-7300-4EE6-8849-46FACE74CA2A"
_INERTIAL_RX = "7DEF8322-7301-4EE6-8849-46FACE74CA2A"


class InertialReader:
    _client: bleak.BleakClient

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        return read_data_by_client(self._client, _INERTIAL_RX)

    def is_connected(self) -> bool:
        return self._client.is_connected
