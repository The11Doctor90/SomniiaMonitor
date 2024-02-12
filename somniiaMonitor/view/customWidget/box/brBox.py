#  Copyright (c) Matteo Ferreri 2024.

import numpy as np
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy_garden.matplotlib import FigureCanvasKivyAgg

from somniiaMonitor.business.plotter import Plotter
from somniiaMonitor.view.customWidget.box.parameterBox import ParameterBox
from somniiaMonitor.view.customWidget.label.titleLabel import TitleLabel
from somniiaMonitor.view.customWidget.label.valueLabel import ValueLabel

def generate_fake_data():
    return np.random.rand()


class BrBox(BoxLayout):
    def __init__(self, **kwargs):
        super(BrBox, self).__init__(**kwargs)
        self._isRunning = False
        self.title = TitleLabel(text='Breath Frequency')
        self.add_widget(self.title)
        self.label = ValueLabel(text='-')
        self.add_widget(self.label)
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        self.label.set_text(generate_fake_data())

    def run(self):
        self._isRunning = True
        self._clock_event = Clock.schedule_interval(self.update_plot, 1)  # Chiamato ogni 1 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            if self._clock_event:
                self._clock_event.cancel()
