#  Copyright (c) Matteo Ferreri 2024.

import numpy as np
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy_garden.matplotlib import FigureCanvasKivyAgg

from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.maskDataReader.temperatureReader import TemperatureReader
from somniiaMonitor.business.model.temperature_business import TemperatureBusiness
from somniiaMonitor.business.plotter import Plotter
from somniiaMonitor.model.temperature_data import TemperatureData
from somniiaMonitor.view.customWidget.box.parameterBox import ParameterBox
from somniiaMonitor.view.customWidget.label.titleLabel import TitleLabel
from somniiaMonitor.view.customWidget.label.valueLabel import ValueLabel


class TemperatureBox(BoxLayout):
    __client: BleClient
    __temperature_reader: TemperatureReader
    __temperature_data: TemperatureData

    def __init__(self, **kwargs):
        super(TemperatureBox, self).__init__(**kwargs)
        self._isRunning = False
        self.__temperature_data = TemperatureData()
        self._temperature_business: TemperatureBusiness = TemperatureBusiness.get_instance()
        self.title = TitleLabel(text='Temperature')
        self.add_widget(self.title)
        self.label = ValueLabel(text='-')
        self.add_widget(self.label)
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        temperature_data = self.read_data()
        self._temperature_business.save_temperature(temperature_data)
        self.label.set_text(f"{temperature_data.get_temperature()} °C")

    def set_analysis_id(self, analysis_id):
        self.__temperature_data.set_analysis_id(analysis_id)

    def set_client(self, client: BleClient):
        self.__client = client

    def read_data(self) -> TemperatureData:
        self.__temperature_reader = TemperatureReader(self.__client.get_client())
        temp_data: TemperatureData = self.__temperature_reader.read()
        temp_data.set_analysis_id(self.__temperature_data.get_analysis_id())
        return temp_data

    def run(self):
        self._isRunning = True
        self._clock_event = Clock.schedule_interval(self.update_plot, 1)  # Chiamato ogni 1 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            self.__temperature_reader.stop()
            if self._clock_event:
                self._clock_event.cancel()
