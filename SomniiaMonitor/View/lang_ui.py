#  Copyright (c) Matteo Ferreri 2024.

# lang_ui.py
from kivy.app import App
from kivy.properties import StringProperty
from lang_observer import Lang


tr = Lang("en")


class LangApp(App):

    lang = StringProperty('en')

    def on_lang(self, instance, lang):
        tr.switch_lang(lang)
