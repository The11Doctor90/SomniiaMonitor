#  Copyright (c) Matteo Ferreri 2024.

from BLEreader import *

_TEMPERATURE_SERVICE = "7DEF8323-7300-4EE6-8849-46FACE74CA2A"
_TEMPERATURE_RX = "7DEF8323-7301-4EE6-8849-46FACE74CA2A"


class TemperatureReader:
    _client: bleak.BleakClient

    def __init__(self, client: bleak.BleakClient):
        self._client = client

    def read(self):
        return read_data_by_client(self._client, _TEMPERATURE_RX)

    def is_connected(self) -> bool:
        return self._client.is_connected
