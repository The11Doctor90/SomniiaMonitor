#  Copyright (c) Matteo Ferreri 2024.

from kivy.uix.label import Label


class ValueLabel(Label):

    def __init__(self, **kwargs):
        super(ValueLabel, self).__init__(**kwargs)

    def set_text(self, text):
        if type(text) != str:
            self.text = str(text)
        else:
            self.text = text
