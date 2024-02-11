#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.maskDataReader.eegReader import EegReader
from somniiaMonitor.business.maskDataReader.ekgReader import EkgReader
from somniiaMonitor.business.maskDataReader.inertialReader import InertialReader
from somniiaMonitor.business.maskDataReader.ppgReader import PpgReader
from somniiaMonitor.business.maskDataReader.stagingReader import StagingReader
from somniiaMonitor.business.maskDataReader.temperatureReader import TemperatureReader
import bleak
import numpy as np


class DataFetchingFromDevice:
    istance = None
    eegReader: EegReader
    ekgReader: EkgReader
    inertialReader: InertialReader
    ppgReader: PpgReader
    stagingReader: StagingReader
    temperatureReader: TemperatureReader
    client: bleak.BleakClient

    def __init__(self, mac: str):
        """init the class responsible for fetching all data from ble device"""
        self.client = bleak.BleakClient(mac)
        self.eegReader = EegReader(self.client)
        self.ekgReader = EkgReader(self.client)
        self.inertialReader = InertialReader(self.client)
        self.ppgReader = PpgReader(self.client)
        self.stagingReader = StagingReader(self.client)
        self.temperatureReader = TemperatureReader(self.client)

    def get_eeg_data(self):
        """ask ble device to send data"""
        return self.eegReader.read()

    def get_ekg_data(self):
        """ask ble device to send data"""
        return self.ekgReader.read()

    def get_inertial_data(self):
        """ask ble device to send data"""
        return self.inertialReader.read()

    def get_ppg_data(self):
        """ask ble device to send data"""
        return self.ppgReader.read()

    def get_staging_data(self):
        """ask ble device to send data"""
        return self.stagingReader.read()

    def get_temperature_data(self):
        """ask ble device to send data"""
        return self.temperatureReader.read()

# def convert_into_array(string: str):
#     """Converte la stringa in ingresso in un array Numpy"""
#
#     array = np.array([number for number in string.split(',')])
#     return array
#
#
# def is_valid(string: str) -> bool:
#     shadow_string = ""
#     if len(string) == 0:
#         return False
#
#     if "," in string:
#         shadow_string = string.replace(',', '')
#     else:
#         shadow_string = string
#
#     if not shadow_string.isnumeric():
#         return False
#
#     shadow_string = string.split(",")
#     if len(shadow_string) != 10:
#         return False
#
#     return True
