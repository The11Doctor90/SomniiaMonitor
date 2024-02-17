#  Copyright (c) Matteo Ferreri 2024.

import numpy as np
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.model.ekg_parameter_data import EkgParameterData
from somniiaMonitor.view.customWidget.label.titleLabel import TitleLabel
from somniiaMonitor.view.customWidget.label.valueLabel import ValueLabel


class HrEkgBox(BoxLayout):
    __ekg_param_data: EkgParameterData

    def __init__(self, **kwargs):
        super(HrEkgBox, self).__init__(**kwargs)
        self._isRunning = False
        self.title = TitleLabel(text='HR EKG')
        self.add_widget(self.title)
        self.label = ValueLabel(text='-')
        self.add_widget(self.label)
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        self.label.set_text(f"{self.__ekg_param_data.get_heart_rate()} BPM")

    def receive(self, ekg_data: EkgParameterData):
        self.__ekg_param_data = ekg_data

    def run(self):
        self._isRunning = True
        self._clock_event = Clock.schedule_interval(self.update_plot, 1)  # Chiamato ogni 1 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            if self._clock_event:
                self._clock_event.cancel()
