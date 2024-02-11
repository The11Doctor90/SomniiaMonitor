#  Copyright (c) Matteo Ferreri 2024.

from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup

import somniiaMonitor.business.maskDataReader.bleReader as ble


class WarningPopup(Popup):
    __instance = None
    warningLabel = ObjectProperty(None)

    # def __init__(self, **kwargs):
    #     super(WarningPopup, self).__init__(**kwargs)

    def __init__(self, **kwargs):
        if WarningPopup.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            super(WarningPopup, self).__init__(**kwargs)
            WarningPopup.__instance = self

    @staticmethod
    def get_instance():
        if WarningPopup.__instance is None:
            WarningPopup()
        return WarningPopup.__instance

    def add_label_text(self, text: str):
        self.label = Label(text=text)
        self.warningLabel.add_widget(self.label)
