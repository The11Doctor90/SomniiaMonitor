# #  Copyright (c) Matteo Ferreri 2024.
#
# from kivy.app import App
# from kivy.properties import StringProperty
# from SomniiaMonitor.Business.lang_observer import Lang
#
# tr = Lang("it")
#
#
# class SomniiaApp(App):
#     lang = StringProperty('it')
#
#     def on_lang(self, instance, lang):
#         tr.switch_lang(lang)
from kivy.app import App
from kivy.properties import BooleanProperty
#  Copyright (c) Matteo Ferreri 2024.

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Start(BoxLayout):
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        App.get_running_app().bind(dayNight=self.switcher_light)

    def switcher_light(self, instance, dayNight):
        print('change background')
        if dayNight:
            self.backgroundColor = (1, 1, 1, 1) #white
            self.toolbarBackgroundColor = (135/255, 206/255, 250/255, 1) #light blue
        else:
            self.backgroundColor = (0, 0, 0, 1) #black
            self.toolbarBackgroundColor = (0,0,40/255, 1) #navy


class CustomLabel(Label):
    def __init__(self, **kwargs):
        super(CustomLabel, self).__init__(**kwargs)
        App.get_running_app().bind(dayNight=self.switcher_light)

    def switcher_light(self, instance, dayNight):
        print('change text')
        if dayNight:
            self.color = (0, 0, 0, 1)
        else:
            self.color = (1, 1, 1, 1)


class ProvaApp(App):
    dayNight = BooleanProperty(None)

    def build(self):
        return
