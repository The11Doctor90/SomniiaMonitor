#  Copyright (c) Matteo Ferreri 2024.
from threading import Thread, Event

import numpy as np
from kivy.clock import Clock
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.eeg_plotter import EegPlotter
from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.maskDataReader.eegReader import EegReader
from somniiaMonitor.business.model.eeg_signal_business import EegSignalBusiness
from somniiaMonitor.business.plotter import Plotter
from somniiaMonitor.model.eeg_signal_data import EegSignalData


class EegGraph(BoxLayout):
    __client: BleClient
    __eeg_reader: EegReader
    __eeg_data: EegSignalData

    def __init__(self, **kwargs):
        super(EegGraph, self).__init__(**kwargs)
        self._anim = None
        self.__eeg_data = EegSignalData()
        self._eeg_signal_business = EegSignalBusiness.get_instance()
        self._plot = EegPlotter()
        self._plot.set_title('EEG Graph')
        self._plot.set_x_axis_name('Time')
        self._plot.add_grid_lines()
        self._canvas = FigureCanvasKivyAgg(self._plot.get_gcf())
        self.add_widget(self._canvas)
        self._isRunning = False
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        eeg_data = self.read_data()
        self._eeg_signal_business.save_inertial_parameter(eeg_data)
        self._plot.add_data(eeg_data)
        self._plot.update_plots(None)  # Chiamiamo manualmente l'aggiornamento del plot
        self._canvas.draw()

    def set_analysis_id(self, analysis_id):
        self.__eeg_data.set_analysis_id(analysis_id)

    def set_client(self, client: BleClient):
        self.__client = client

    def read_data(self) -> EegSignalData:
        self.__eeg_reader = EegReader(self.__client.get_client())
        eeg_data: EegSignalData = self.__eeg_reader.read()
        eeg_data.set_analysis_id(self.__eeg_data.get_analysis_id())
        return eeg_data

    def run(self):
        self._isRunning = True
        self._plot.init_plot()  # Inizializziamo il plot
        self._clock_event = Clock.schedule_interval(self.update_plot, 0.2)  # Chiamato ogni 0.2 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            self.__eeg_reader.stop()
            if self._clock_event:
                self._clock_event.cancel()
