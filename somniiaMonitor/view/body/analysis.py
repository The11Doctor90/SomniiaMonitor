#  Copyright (c) Matteo Ferreri 2024.
import time
from threading import Thread

from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

import somniiaMonitor.business.maskDataReader.bleReader as ble


class AnalysisScreen(Screen):
    inertial = ObjectProperty(None)
    ekg = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(AnalysisScreen, self).__init__(**kwargs)

    def run(self):
        self.inertial.run()
        self.ekg.run()

    def stop(self):
        self.inertial.stop()
        self.ekg.stop()
