#  Copyright (c) Matteo Ferreri 2024.
import time
from threading import Thread, Event

import numpy as np
from kivy.clock import Clock
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.plotter import Plotter


def generate_fake_data():
    return np.random.rand()


class EkgGraph(BoxLayout):

    def __init__(self, **kwargs):
        super(EkgGraph, self).__init__(**kwargs)
        self._anim = None
        self._plot = Plotter()
        self._canvas = FigureCanvasKivyAgg(self._plot.get_gcf())
        self.add_widget(self._canvas)
        self._isRunning = False
        self._clock_event = None  # Per tenere traccia dell'evento del clock

    def update_plot(self, dt):
        self._plot.add_data(generate_fake_data(), generate_fake_data())
        self._plot.update_plots(None)  # Chiamiamo manualmente l'aggiornamento del plot
        self._canvas.draw()

    def run(self):
        self._isRunning = True
        self._plot.init_plot()  # Inizializziamo il plot
        self._clock_event = Clock.schedule_interval(self.update_plot, 0.2)  # Chiamato ogni 0.2 secondi

    def stop(self):
        if self._isRunning:
            self._isRunning = False
            if self._clock_event:
                self._clock_event.cancel()
