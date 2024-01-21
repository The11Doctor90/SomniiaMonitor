#  Copyright (c) Matteo Ferreri 2024.
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

kivy.require('2.3.0')


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

    def click_button(self):
        app = App.get_running_app()
        sm = app.root.ids.sm
        sm.current = 'second_screen'


class SecondScreen(Screen):
    pass


class SomniiaApp(App):
    def build(self):
        self.title = 'screen with header and footer'
        return Builder.load_file('SomniiaMonitor/View/somniia.kv')
