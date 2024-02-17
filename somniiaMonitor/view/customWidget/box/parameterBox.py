#  Copyright (c) Matteo Ferreri 2024.
from threading import Thread, Event

import numpy as np
from kivy.clock import Clock
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout

from somniiaMonitor.business.plotter import Plotter

count = 0

def generate_fake_data():
    return np.random.rand()


class ParameterBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ParameterBox, self).__init__(**kwargs)
