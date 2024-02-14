#  Copyright (c) Matteo Ferreri 2024.

from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

import somniiaMonitor.business.maskDataReader.bleReader as ble
from somniiaMonitor.business.model.mask_business import MaskBusiness
from somniiaMonitor.model.mask import Mask
from somniiaMonitor.view.customWidget.button.deviceButton import DeviceButton
from somniiaMonitor.view.customWidget.popup.warningPopup import WarningPopup


class BleSearchPopup(Popup):
    bleSearch = ObjectProperty(None)
    foundedBleList = ObjectProperty(None)

    mask_business: MaskBusiness = MaskBusiness.get_instance()
    def __init__(self, **kwargs):
        super(BleSearchPopup, self).__init__(**kwargs)

    def search(self):
        try:
            devices = ble.find_all_device()
            self.h = self.height = 0.9
            for i, device_info in enumerate(devices):
                # self.h = self.h + self.height * 0.1
                # self.btn = Button(text=device_info.name, on_release=self.mask_business.save_mask(mask))
                self.btn = DeviceButton(size_hint=(None, None), size=(100, 50))
                self.btn.set_mask(device_info.address, device_info.name)

                self.foundedBleList.add_widget(self.btn)
        except Exception as e:
            Popup(title='Warning', content=Label(text='No bluetooth adapters found'), size_hint=(None, None),
                  size=(300, 200)).open()
            # self.warning = WarningPopup.get_instance()
            # self.warning.add_label_text('No bluetooth adapters found')
            # self.warning.open()

