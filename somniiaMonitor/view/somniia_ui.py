#  Copyright (c) Matteo Ferreri 2024.

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.utils import platform

from somniiaMonitor.business.lang_observer import Lang
from somniiaMonitor.view.allWidgetImported import *   #NON CANCELLARE!!! Importa tutti i widget customizzati che altrimenti dovrebbero stare in questo file

kivy.require('2.3.0')

tr = Lang("it")

class SomniiaApp(App):
    lang = StringProperty('it')

    pl_name = platform  # OS identify
    print(f'kivy: {pl_name}')

    def build(self):
        self.title = "Somniia Monitor"
        return Builder.load_file('somniiaMonitor/view/somniia.kv')

    def on_lang(self, instance, lang):
        tr.switch_lang(lang)
