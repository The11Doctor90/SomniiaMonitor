#  Copyright (c) Matteo Ferreri 2024.
from kivy.clock import Clock

from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.maskDataReader.ekgParamReader import EkgParamReader
from somniiaMonitor.business.model.ekg_parameter_business import EkgParameterBusiness
from somniiaMonitor.model.ekg_parameter_data import EkgParameterData


class EkgParamPublisher:
    __client: BleClient
    __ekg_param_reader: EkgParamReader
    __ekg_param_data: EkgParameterData

    def __init__(self):
        self.__ekg_param_data = EkgParameterData()
        self.__ekg_param_business: EkgParameterBusiness = EkgParameterBusiness.get_instance()
        self.__subscribers = []
        self._clock_event = None

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def update_plot(self, dt):
        ekg_data = self.read_data()
        self.__ekg_param_business.save_ekg_parameter(ekg_data)
        for subscriber in self.__subscribers:
            subscriber.receive(ekg_data)

    def set_analysis_id(self, analysis_id):
        self.__ekg_param_data.set_analysis_id(analysis_id)

    def set_client(self, client: BleClient):
        self.__client = client

    def read_data(self) -> EkgParameterData:
        self.__ekg_param_reader = EkgParamReader(self.__client.get_client())
        ekg_data: EkgParameterData = self.__ekg_param_reader.read()
        ekg_data.set_analysis_id(self.__ekg_param_data.get_analysis_id())
        return ekg_data

    def run(self):
        self._clock_event = Clock.schedule_interval(self.update_plot, 1)
        for subscriber in self.__subscribers:
            subscriber.run()

    def stop(self):
        for subscriber in self.__subscribers:
            subscriber.stop()
        self.__ekg_param_reader.stop()
        if self._clock_event:
            self._clock_event.cancel()
