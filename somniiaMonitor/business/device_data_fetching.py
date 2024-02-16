#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.maskDataReader.eegReader import EegReader
from somniiaMonitor.business.maskDataReader.ekgSignalReader import EkgSignalReader
from somniiaMonitor.business.maskDataReader.inertialReader import InertialReader
from somniiaMonitor.business.maskDataReader.ppgReader import PpgReader
from somniiaMonitor.business.maskDataReader.stagingReader import StagingReader
from somniiaMonitor.business.maskDataReader.temperatureReader import TemperatureReader

from somniiaMonitor.business.model.eeg_signal_business import EegSignalBusiness
from somniiaMonitor.business.model.ekg_parameter_business import EkgParameterBusiness
from somniiaMonitor.business.model.inertial_parameter_business import InertialParameterBusiness
from somniiaMonitor.business.model.ppg_parameter_business import PpgParameterBusiness
from somniiaMonitor.business.model.sleep_stage_business import SleepStageBusiness
from somniiaMonitor.business.model.temperature_business import TemperatureBusiness
import bleak
import numpy as np


class DataFetchingFromDevice:
    eegReader: EegReader
    ekgReader: EkgSignalReader
    inertialReader: InertialReader
    ppgReader: PpgReader
    stagingReader: StagingReader
    temperatureReader: TemperatureReader
    client: bleak.BleakClient

    eegSignalBusiness: EegSignalBusiness
    ekgParameterBusiness: EkgParameterBusiness
    inertialParameterBusiness: InertialParameterBusiness
    ppgParameterBusiness: PpgParameterBusiness
    stagingParameterBusiness: SleepStageBusiness
    temperatureParameterBusiness: TemperatureBusiness

    def __init__(self, mac: str):
        """init the class responsible for fetching all data from ble device"""
        self.client = bleak.BleakClient(mac)
        self.eegReader = EegReader(self.client)
        self.ekgReader = EkgSignalReader(self.client)
        self.inertialReader = InertialReader(self.client)
        self.ppgReader = PpgReader(self.client)
        self.stagingReader = StagingReader(self.client)
        self.temperatureReader = TemperatureReader(self.client)

        self.eegSignalBusiness = EegSignalBusiness.get_instance()

    def get_eeg_data(self, analysis_id: int):
        """ask ble device to send data"""
        data = self.eegReader.read()
        data.set_analysis_id(analysis_id)
        self.eegSignalBusiness.save_eeg_signal(data)
        return data

    def get_ekg_data(self, analysis_id: int):
        """ask ble device to send data"""
        data = self.ekgReader.read()
        data.set_analysis_id(analysis_id)
        self.ekgParameterBusiness.save_ekg_parameter(data)
        return data

    def get_inertial_data(self, analysis_id: int):
        """ask ble device to send data"""
        data = self.inertialReader.read()
        data.set_analysis_id(analysis_id)
        self.inertialParameterBusiness.save_inertial_parameter(data)
        return data

    def get_ppg_data(self, analysis_id: int):
        """ask ble device to send data"""
        data = self.ppgReader.read()
        data.set_analysis_id(analysis_id)
        self.ppgParameterBusiness.save_ppg_parameter(data)
        return data

    def get_staging_data(self, analysis_id: int):
        """ask ble device to send data"""
        data = self.stagingReader.read()
        data.set_analysis_id(analysis_id)
        self.stagingParameterBusiness.save_sleep_stage(data)
        return data

    def get_temperature_data(self, analysis_id: int):
        """ask ble device to send data"""
        data = self.temperatureReader.read()
        data.set_analysis_id(analysis_id)
        self.temperatureParameterBusiness.save_temperature(data)
        return data

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
