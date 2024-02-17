#  Copyright (c) Matteo Ferreri 2024.

from kivy.clock import Clock
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.maskDataReader.stagingReader import StagingReader
from somniiaMonitor.business.model.sleep_stage_business import SleepStageBusiness
from somniiaMonitor.business.plotter import Plotter
from somniiaMonitor.model.sleep_stage_data import SleepStageData


class StagingGraph(BoxLayout):
    __client: BleClient
    __staging_reader: StagingReader
    __staging_data: SleepStageData
    _staging_business: SleepStageBusiness

    def __init__(self, **kwargs):
        super(StagingGraph, self).__init__(**kwargs)
        self._anim = None
        self.__staging_data = SleepStageData()
        self._staging_business = SleepStageBusiness.get_instance()
        self._plot = Plotter()
        self._plot.set_title('Staging Graph')
        self._plot.set_y_axis_name('Stage')
        self._plot.add_grid_lines()
        self._canvas = FigureCanvasKivyAgg(self._plot.get_gcf())
        self.add_widget(self._canvas)
        self._isRunning = False
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        staging_data = self.read_data()
        self._staging_business.save_sleep_stage(staging_data)
        self._plot.add_data(int(staging_data.get_time()), int(staging_data.get_stage()))
        self._plot.update_plots(None)  # Chiamiamo manualmente l'aggiornamento del plot
        self._canvas.draw()

    def set_analysis_id(self, analysis_id):
        self.__staging_data.set_analysis_id(analysis_id)

    def set_client(self, client: BleClient):
        self.__client = client

    def read_data(self) -> SleepStageData:
        self.__staging_reader = StagingReader(self.__client.get_client())
        staging_data: SleepStageData = self.__staging_reader.read()
        staging_data.set_analysis_id(self.__staging_data.get_analysis_id())
        return staging_data

    def run(self):
        self._isRunning = True
        self._plot.init_plot()  # Inizializziamo il plot
        self._clock_event = Clock.schedule_interval(self.update_plot, 0.002)  # Chiamato ogni 0.2 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            self.__staging_reader.stop()
            if self._clock_event:
                self._clock_event.cancel()
