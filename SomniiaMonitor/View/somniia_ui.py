#  Copyright (c) Matteo Ferreri 2024.
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from SomniiaMonitor.Business.lang_observer import Lang

kivy.require('2.3.0')

tr = Lang("it")


class MainWindow(BoxLayout):
    # def __init__(self, **kwargs):
    #     super(MainWindow, self).__init__(**kwargs)
    pass


class SomniiaApp(App):
    lang = StringProperty('it')

    pl_name = platform  # OS identify
    print(f'kivy: {pl_name}')

    def build(self):
        self.title = "Somniia Monitor"
        return Builder.load_file('SomniiaMonitor/View/somniia.kv')

    def on_lang(self, instance, lang):
        tr.switch_lang(lang)
