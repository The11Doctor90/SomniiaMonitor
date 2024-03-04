#  Copyright (c) Matteo Ferreri 2024.
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from somniiaMonitor.business.model.contact_business import ContactBusiness
from somniiaMonitor.business.model.user_business import UserBusiness
from somniiaMonitor.business.model.user_session import UserSessionManager
from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.sleeper import Sleeper

user_business: UserBusiness = UserBusiness.get_instance()
session: UserSessionManager = UserSessionManager.get_instance()


class SleeperRegistration(Screen):
    email_text = ObjectProperty(None)
    password_text = ObjectProperty(None)

    __sleeper: Sleeper
    __contact: Contact

    def __init__(self, **kwargs):
        super(SleeperRegistration, self).__init__(**kwargs)
        self.__sleeper = Sleeper()
        self.__contact = Contact()

    def login(self):
        self._build_sleeper()
        try:
            response = user_business.login(email=self.email_text.text, password=self.password_text.text)
            if response.get_object() is not None:
                session.set_session(response.get_object())
                print("utente loggato")
                Popup(title='Success', content=Label(text=response.get_message()), size_hint=(None, None),
                      size=(300, 200)).open()

        except Exception as e:
            Popup(title='Warning', content=Label(text=response.get_message()), size_hint=(None, None),
                  size=(300, 200)).open()
            print("popup: Utente non loggato")


