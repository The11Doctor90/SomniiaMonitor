#  Copyright (c) Matteo Ferreri 2024.
from kivy.clock import Clock

from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.maskDataReader.ppgReader import PpgReader
from somniiaMonitor.business.model.ppg_parameter_business import PpgParameterBusiness
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData


class PpgParamPublisher:
    __client: BleClient
    __ppg_param_reader: PpgReader
    __ppg_param_data: PpgParameterData

    def __init__(self):
        self.__ppg_param_data = PpgParameterData()
        self.__ppg_param_business: PpgParameterBusiness = PpgParameterBusiness.get_instance()
        self.__subscribers = []
        self._clock_event = None

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def update_plot(self, dt):
        ppg_data = self.read_data()
        self.__ppg_param_business.save_ppg_parameter(ppg_data)
        for subscriber in self.__subscribers:
            subscriber.receive(ppg_data)

    def set_analysis_id(self, analysis_id):
        self.__ppg_param_data.set_analysis_id(analysis_id)

    def set_client(self, client: BleClient):
        self.__client = client

    def read_data(self) -> PpgParameterData:
        self.__ppg_param_reader = PpgReader(self.__client.get_client())
        ppg_data: PpgParameterData = self.__ppg_param_reader.read()
        ppg_data.set_analysis_id(self.__ppg_param_data.get_analysis_id())
        return ppg_data

    def run(self):
        self._clock_event = Clock.schedule_interval(self.update_plot, 1)
        for subscriber in self.__subscribers:
            subscriber.run()

    def stop(self):
        for subscriber in self.__subscribers:
            subscriber.stop()
        self.__ppg_param_reader.stop()
        if self._clock_event:
            self._clock_event.cancel()
