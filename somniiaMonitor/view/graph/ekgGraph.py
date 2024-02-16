#  Copyright (c) Matteo Ferreri 2024.

from kivy.clock import Clock
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.maskDataReader.ekgSignalReader import EkgSignalReader
from somniiaMonitor.business.model.ekg_signal_business import EkgSignalBusiness
from somniiaMonitor.business.plotter import Plotter
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgGraph(BoxLayout):
    __client: BleClient
    __ekg_signal_reader: EkgSignalReader
    __ekg_signal_data: EkgSignalData

    def __init__(self, **kwargs):
        super(EkgGraph, self).__init__(**kwargs)
        self._anim = None
        self.__ekg_signal_data = EkgSignalData()
        self._ekg_signal_business: EkgSignalBusiness = EkgSignalBusiness.get_instance()
        self._plot = Plotter()
        self._plot.set_title('EKG Graph')
        self._plot.set_x_axis_name('Time')
        self._plot.add_grid_lines()
        self._canvas = FigureCanvasKivyAgg(self._plot.get_gcf())
        self.add_widget(self._canvas)
        self._isRunning = False
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        ekg_signal_data = self.read_data()
        self._ekg_signal_business.save_ekg_signal(ekg_signal_data)
        self._plot.add_data(int(ekg_signal_data.get_time()), int(ekg_signal_data.get_signal()))
        self._plot.update_plots(None)  # Chiamiamo manualmente l'aggiornamento del plot
        self._canvas.draw()

    def set_analysis_id(self, analysis_id):
        self.__ekg_signal_data.set_analysis_id(analysis_id)

    def set_client(self, client: BleClient):
        self.__client = client

    def read_data(self) -> EkgSignalData:
        self.__ekg_signal_reader = EkgSignalReader(self.__client.get_client())
        ekg_signal_data: EkgSignalData = self.__ekg_signal_reader.read()
        ekg_signal_data.set_analysis_id(self.__ekg_signal_data.get_analysis_id())
        return ekg_signal_data

    def run(self):
        self._isRunning = True
        self._plot.init_plot()  # Inizializziamo il plot
        self._clock_event = Clock.schedule_interval(self.update_plot, 0.2)  # Chiamato ogni 0.2 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            self.__ekg_signal_reader.stop()
            if self._clock_event:
                self._clock_event.cancel()
