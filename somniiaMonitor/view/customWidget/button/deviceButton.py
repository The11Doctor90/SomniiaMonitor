#  Copyright (c) Matteo Ferreri 2024.

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from somniiaMonitor.business.model.mask_business import MaskBusiness
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.mask import Mask


class DeviceButton(Button):
    mask = Mask()
    mask_business = MaskBusiness.get_instance()

    def __init__(self, **kwargs):
        super(DeviceButton, self).__init__(**kwargs)

    def set_mask(self, mac_address: str, name: str):
        self.mask.set_mac_addr(mac_address)
        self.mask.set_name(name)
        self.set_text(name)

    def set_text(self, text: str) -> None:
        self.text = text

    def on_release(self):
        try:
            response: ActionResponse = self.mask_business.save_mask(self.mask)
            if response.get_row_count() > 0:
                Popup(title='Success', content=Label(text='Device Saved'), size_hint=(None, None),
                      size=(300, 200)).open()
        except Exception as e:
            Popup(title='Warning', content=Label(text='Impossible to save device'), size_hint=(None, None),
                  size=(300, 200)).open()
