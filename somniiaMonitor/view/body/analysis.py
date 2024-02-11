#  Copyright (c) Matteo Ferreri 2024.

from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from somniiaMonitor.model.mask import Mask


class AnalysisScreen(Screen):
    inertial = ObjectProperty(None)
    ekg = ObjectProperty(None)
    mask = Mask()
    mask_collegato = True
    is_attivo = False

    def __init__(self, **kwargs):
        super(AnalysisScreen, self).__init__(**kwargs)

    def run(self):
        if self.is_attivo:
            return
        # TODO: set the macAddress corretto
        self.mask.set_mac_addr("hello world")
        print("wiii mi sto collegando al BLE")
        print("faccio finta di essere collegato <3")
        if self.mask_collegato:
            self.is_attivo = True
            self.inertial.run()
            self.ekg.run()
        else:
            Popup(title='Warning', content=Label(text='No connected devices'), size_hint=(None, None), size=(300, 200)).open()
            print("popup: no connected devices")  # TODO

    def stop(self):
        if self.is_attivo:
            self.is_attivo = False
            self.inertial.stop()
            self.ekg.stop()
