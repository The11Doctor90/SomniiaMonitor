#  Copyright (c) Matteo Ferreri 2024.

from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.inertial_plotter import InertialPlotter
from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.maskDataReader.inertialReader import InertialReader
from somniiaMonitor.business.model.inertial_parameter_business import InertialParameterBusiness
from somniiaMonitor.business.plotter import Plotter
from somniiaMonitor.model.inertial_parameter_data import InertialParameterData


class InertialGraph(BoxLayout):
    __client: BleClient
    __inertial_reader: InertialReader
    __inertial_data: InertialParameterData

    ck_rms = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(InertialGraph, self).__init__(**kwargs)
        self._anim = None
        self.__inertial_data = InertialParameterData()
        self._inertial_business = InertialParameterBusiness.get_instance()
        self._plot = InertialPlotter()
        self._plot.set_title('Inertial Graph')
        self._plot.set_x_axis_name('Time')
        self._plot.add_grid_lines()
        self._canvas = FigureCanvasKivyAgg(self._plot.get_gcf())
        self.add_widget(self._canvas)
        self._isRunning = False
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        inertial_data = self.read_data()
        self._inertial_business.save_inertial_parameter(inertial_data)
        self._plot.add_data(inertial_data)
        self._plot.update_plots(None)  # Chiamiamo manualmente l'aggiornamento del plot
        self._canvas.draw()

    def set_analysis_id(self, analysis_id):
        self.__inertial_data.set_analysis_id(analysis_id)

    def set_client(self, client: BleClient):
        self.__client = client

    def read_data(self) -> InertialParameterData:
        self.__inertial_reader = InertialReader(self.__client.get_client())
        inertial_data: InertialParameterData = self.__inertial_reader.read()
        inertial_data.set_analysis_id(self.__inertial_data.get_analysis_id())
        return inertial_data

    def run(self):
        self._isRunning = True
        self._plot.init_plot()  # Inizializziamo il plot
        self._clock_event = Clock.schedule_interval(self.update_plot, 0.2)  # Chiamato ogni 0.2 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            self.__inertial_reader.stop()
            if self._clock_event:
                self._clock_event.cancel()

    def set_rms_visible(self):
        self._plot.set_rms_visible()

    def set_roll_visible(self):
        self._plot.set_roll_visible()

    def set_pitch_visible(self):
        self._plot.set_pitch_visible()

    def set_yaw_visible(self):
        self._plot.set_yaw_visible()
