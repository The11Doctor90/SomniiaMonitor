#  Copyright (c) Matteo Ferreri 2024.

from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

import somniiaMonitor.business.maskDataReader.bleReader as ble


class BleSearchPopup(Popup):
    bleSearch = ObjectProperty(None)
    foundedBleList = ObjectProperty(None)

    # bleList = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(BleSearchPopup, self).__init__(**kwargs)

    def search(self):
        try:
            devices = ble.find_all_device()
            self.h = self.height = 0.9
            for i, device_info in enumerate(devices):
                self.h = self.h + self.height * 0.1
                self.btn = Button(text=device_info.name)
                self.foundedBleList.add_widget(self.btn)
        except Exception as e:
            Popup(title='Warning', content=Label(text='No bluetooth adapters found'), size_hint=(None, None),
                  size=(300, 200)).open()
            # self.warning = WarningPopup.get_instance()
            # self.warning.add_label_text("ciaoco")
            # self.foundedBleList.add_widget(self.warning)

            # self.warning = WarningPopup()
            # self.warning.add_label_text("ciaoco")
            # self.foundedBleList.add_widget(self.warning)
