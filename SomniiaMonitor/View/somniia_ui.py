#  Copyright (c) Matteo Ferreri 2024.

from kivy.app import App
from kivy.properties import StringProperty
from kivy.utils import platform
from kivy.lang import Builder
from SomniiaMonitor.Business.lang_observer import Lang

tr = Lang("it")


class SomniiaApp(App):
    lang = StringProperty('it')

    pl_name = platform #OS identify
    print(f'kivy: {pl_name}')

    def build(self):
        return Builder.load_file('SomniiaMonitor/View/somniia.kv')

    def on_lang(self, instance, lang):
        tr.switch_lang(lang)
