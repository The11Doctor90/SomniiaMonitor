#  Copyright (c) Matteo Ferreri 2024.

import numpy as np
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from somniiaMonitor.business.maskDataReader.ble_client import BleClient
from somniiaMonitor.business.model.analysis_business import AnalysisBusiness
from somniiaMonitor.business.model.mask_business import MaskBusiness
from somniiaMonitor.business.model.user_business import UserBusiness
from somniiaMonitor.model.analysis import Analysis
from somniiaMonitor.model.mask import Mask
from somniiaMonitor.view.ekgParamPublisher import EkgParamPublisher
from somniiaMonitor.view.ppgParamPublisher import PpgParamPublisher


def generate_fake_data():
    return np.random.rand()

analyses = Analysis()
analyses.set_doctor_id(1)
analyses.set_sleeper_id(1)
analyses.set_mask_id(1)
analyses.set_code(str(generate_fake_data()))

mask = Mask()

analysis_business: AnalysisBusiness = AnalysisBusiness.get_instance()
user_business: UserBusiness = UserBusiness.get_instance()
mask_business: MaskBusiness = MaskBusiness.get_instance()
# data_fetch = DataFetchingFromDevice()
mac_addr = "59:6B:66:30:04:EA"

class AnalysisScreen(Screen):
    inertial = ObjectProperty(None)
    ekg = ObjectProperty(None)
    eeg = ObjectProperty(None)
    staging = ObjectProperty(None)
    hr_ekg = ObjectProperty(None)
    hr_ppg = ObjectProperty(None)
    hrv = ObjectProperty(None)
    rr = ObjectProperty(None)
    temp = ObjectProperty(None)
    spo2 = ObjectProperty(None)
    pi = ObjectProperty(None)
    br = ObjectProperty(None)

    mask_collegato = True
    is_attivo = False

    def __init__(self, **kwargs):
        super(AnalysisScreen, self).__init__(**kwargs)
        self.ekg_publisher = EkgParamPublisher()
        self.ppg_publisher = PpgParamPublisher()
        # self.dropdown = DropDown()
        # for i in range(10):
        #     btn = Button(text="%d" % i, size_hint_y=None, height=44)
        #     btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
        #     self.dropdown.add_widget(btn)
        # mainBtn = Button(text="Hello", size_hint=(None, None))
        # mainBtn.bind(on_release=self.dropdown.open)
        # self.dropdown.bind(on_select=lambda instance, x: setattr(mainBtn, 'text', x))

    def run(self):
        # try:
        response = analysis_business.save_analysis(analyses)
        if response.get_row_count() > 0:
            analysis = response.get_object()
            self.inertial.set_analysis_id(analysis.get_analysis_id())
            self.ekg.set_analysis_id(analysis.get_analysis_id())
            self.staging.set_analysis_id(analysis.get_analysis_id())
            self.eeg.set_analysis_id(analysis.get_analysis_id())
            self.ekg_publisher.set_analysis_id(analysis.get_analysis_id())
            self.ppg_publisher.set_analysis_id(analysis.get_analysis_id())
            self.client = BleClient(mac_addr)
            self._deploy_client()
            self._ekg_param_subscribe()
            self._run()
        # except Exception as e:
        #     Popup(title='Warning', content=Label(text='No analysis'), size_hint=(None, None),
        #           size=(300, 200)).open()
        #     print("popup: No analysis")

    def _run(self):
        if self.is_attivo:
            return
        if self.mask_collegato:
            self.is_attivo = True
            self.inertial.run()
            self.ekg.run()
            self.staging.run()
            self.eeg.run()
            self.ekg_publisher.run()
            self.ppg_publisher.run()
            self.temp.run()
        else:
            Popup(title='Warning', content=Label(text='No connected devices'), size_hint=(None, None),
                  size=(300, 200)).open()

    def stop(self):
        if self.is_attivo:
            self.is_attivo = False
            self.inertial.stop()
            self.ekg.stop()
            self.staging.stop()
            self.eeg.stop()
            self.ekg_publisher.stop()
            self.ppg_publisher.stop()
            self.temp.stop()
            self.client.close_connection()

    def _deploy_client(self):
        self.ekg.set_client(self.client)
        self.staging.set_client(self.client)
        self.ekg_publisher.set_client(self.client)
        self.ppg_publisher.set_client(self.client)
        self.eeg.set_client(self.client)
        self.temp.set_client(self.client)
        self.inertial.set_client(self.client)

    def _ekg_param_subscribe(self):
        self.ekg_publisher.subscribe(self.hr_ekg)
        self.ekg_publisher.subscribe(self.hrv)
        self.ekg_publisher.subscribe(self.rr)

    def _ppg_param_subscribe(self):
        self.ppg_publisher.subscribe(self.hr_ppg)
        self.ppg_publisher.subscribe(self.spo2)
        self.ppg_publisher.subscribe(self.pi)
        self.ppg_publisher.subscribe(self.br)



















