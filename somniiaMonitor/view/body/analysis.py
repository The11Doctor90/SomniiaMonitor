#  Copyright (c) Matteo Ferreri 2024.

from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from somniiaMonitor.business.dataFetchingFromDevice import DataFetchingFromDevice
from somniiaMonitor.business.model.analysis_business import AnalysisBusiness
from somniiaMonitor.model.analysis import Analysis
from somniiaMonitor.model.mask import Mask

analysis = Analysis()
analysis.set_analysis_id(3)
analysis.set_doctor_id(4)
analysis.set_sleeper_id(1)
analysis.set_mask_id(1)

analysis_business: AnalysisBusiness = AnalysisBusiness.get_instance()
# data_fetch = DataFetchingFromDevice()


class AnalysisScreen(Screen):
    inertial = ObjectProperty(None)
    ekg = ObjectProperty(None)
    eeg = ObjectProperty(None)
    staging = ObjectProperty(None)
    hr_ekg = ObjectProperty(None)
    mask = Mask()
    mask_collegato = True
    is_attivo = False

    def __init__(self, **kwargs):
        super(AnalysisScreen, self).__init__(**kwargs)

    def run(self):
        try:
            response = analysis_business.save_analysis(analysis)
            if response.get_row_count() > 0:
                self.inertial.set_analysis_id(analysis.get_analysis_id())
                self.ekg.set_analysis_id(analysis.get_analysis_id())
                self.staging.set_analysis_id(analysis.get_analysis_id())
                self.eeg.set_analysis_id(analysis.get_analysis_id())
                self._run()
        except Exception as e:
            Popup(title='Warning', content=Label(text='No analysis'), size_hint=(None, None),
                  size=(300, 200)).open()
            print("popup: No analysis")

    def _run(self):
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
            self.staging.run()
            self.eeg.run()
            self.hr_ekg.run()
        else:
            Popup(title='Warning', content=Label(text='No connected devices'), size_hint=(None, None),
                  size=(300, 200)).open()
            print("popup: no connected devices")  # TODO

    def stop(self):
        if self.is_attivo:
            self.is_attivo = False
            self.inertial.stop()
            self.ekg.stop()
            self.staging.stop()
            self.eeg.stop()
            self.hr_ekg.stop()
