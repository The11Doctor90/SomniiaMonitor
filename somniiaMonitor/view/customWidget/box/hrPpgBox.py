#  Copyright (c) Matteo Ferreri 2024.

import numpy as np
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData
from somniiaMonitor.view.customWidget.label.titleLabel import TitleLabel
from somniiaMonitor.view.customWidget.label.valueLabel import ValueLabel


class HrPpgBox(BoxLayout):
    __ppg_param_data: PpgParameterData

    def __init__(self, **kwargs):
        super(HrPpgBox, self).__init__(**kwargs)
        self._isRunning = False
        self.title = TitleLabel(text='HR PPG')
        self.add_widget(self.title)
        self.label = ValueLabel(text='-')
        self.add_widget(self.label)
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        self.label.set_text(f"{self.__ppg_param_data.get_heart_rate()} BPM")

    def receive(self, ppg_data: PpgParameterData):
        self.__ppg_param_data = ppg_data

    def run(self):
        self._isRunning = True
        self._clock_event = Clock.schedule_interval(self.update_plot, 1)  # Chiamato ogni 1 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            if self._clock_event:
                self._clock_event.cancel()
