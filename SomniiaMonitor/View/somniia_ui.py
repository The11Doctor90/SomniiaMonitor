#  Copyright (c) Matteo Ferreri 2024.

from kivy.app import App
from kivy.properties import StringProperty
from SomniiaMonitor.Business.lang_observer import Lang

tr = Lang("it")


class SomniiaApp(App):
    lang = StringProperty('it')

    def on_lang(self, instance, lang):
        tr.switch_lang(lang)
