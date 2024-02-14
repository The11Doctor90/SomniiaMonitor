#  Copyright (c) Matteo Ferreri 2024.
from threading import Thread, Event

import numpy as np
from bleak import BleakClient
from kivy.clock import Clock
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.maskDataReader.inertialReader import InertialReader
from somniiaMonitor.business.plotter import Plotter
from somniiaMonitor.model.inertial_parameter_data import InertialParameterData

count = 0

def generate_fake_data():
    return np.random.rand()


class InertialGraph(BoxLayout):
    __client: BleakClient

    def __init__(self, **kwargs):
        super(InertialGraph, self).__init__(**kwargs)
        self._anim = None

        self._plot = Plotter()
        self._canvas = FigureCanvasKivyAgg(self._plot.get_gcf())
        self.add_widget(self._canvas)
        self._isRunning = False
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        global count
        inertial_data = self.read_data()
        self._plot.add_data(inertial_data.get_time(), inertial_data.get_roll())
        self._plot.update_plots(None)  # Chiamiamo manualmente l'aggiornamento del plot
        self._canvas.draw()
        count += 1

    def set_analysis_id(self, analysis_id):
        print("Intertial Analysis ID: ", analysis_id)

    def set_client(self, client: BleakClient):
        self.__client = client

    def read_data(self) -> InertialParameterData:
        inertial_reader = InertialReader(self.__client)
        return inertial_reader.read()

    def run(self):
        self._isRunning = True
        self._plot.init_plot()  # Inizializziamo il plot
        self._clock_event = Clock.schedule_interval(self.update_plot, 0.2)  # Chiamato ogni 0.2 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            if self._clock_event:
                self._clock_event.cancel()


