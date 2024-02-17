#  Copyright (c) Matteo Ferreri 2024.
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from somniiaMonitor.business.model.contact_business import ContactBusiness
from somniiaMonitor.business.model.user_business import UserBusiness
from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.sleeper import Sleeper

user_business: UserBusiness = UserBusiness.get_instance()
contact_business: ContactBusiness = ContactBusiness.get_instance()


class SleeperRegistration(Screen):
    nametext = ObjectProperty(None)
    surnametext = ObjectProperty(None)
    taxtext = ObjectProperty(None)
    birthtext = ObjectProperty(None)
    gendertext = ObjectProperty(None)
    emailtext = ObjectProperty(None)
    passwordtext = ObjectProperty(None)
    phonetext = ObjectProperty(None)
    addresstext = ObjectProperty(None)
    numbertext = ObjectProperty(None)
    citytext = ObjectProperty(None)
    provtext = ObjectProperty(None)
    zipcodetext = ObjectProperty(None)
    countrytext = ObjectProperty(None)
    save = ObjectProperty(None)
    back = ObjectProperty(None)

    __sleeper: Sleeper
    __contact: Contact

    def __init__(self, **kwargs):
        super(SleeperRegistration, self).__init__(**kwargs)
        self.__sleeper = Sleeper()
        self.__contact = Contact()

    def save_Sleeper(self):
        self._build_sleeper()
        try:
            response = user_business.save_sleeper(sleeper=self.__sleeper)
            if response.get_row_count() > 0:
                self.__sleeper = response.get_object()
                self._build_contact()
                response = contact_business.save_contact(contact=self.__contact)
                if response.get_row_count() > 0:
                    Popup(title='Success', content=Label(text='User Saved'), size_hint=(None, None),
                          size=(300, 200)).open()

        except Exception as e:
            Popup(title='Warning', content=Label(text='User Unsaved'), size_hint=(None, None),
                  size=(300, 200)).open()
            print("popup: User Unsaved")

    def _build_sleeper(self):
        self.__sleeper.set_name(self.nametext.text)
        self.__sleeper.set_surname(self.surnametext.text)
        self.__sleeper.set_tax_id(self.taxtext.text)
        self.__sleeper.set_birth_date(self.birthtext.text)
        self.__sleeper.set_gender(self.gendertext.text)
        self.__sleeper.set_password(self.passwordtext.text)

    def _build_contact(self):
        self.__contact.set_user_id(self.__sleeper.get_user_id())
        self.__contact.set_email(self.emailtext.text)
        self.__contact.set_phone(self.phonetext.text)
        self.__contact.set_address(self.addresstext.text)
        self.__contact.set_number(self.numbertext.text)
        self.__contact.set_city(self.citytext.text)
        self.__contact.set_province(self.provtext.text)
        self.__contact.set_zip_code(self.zipcodetext.text)
        self.__contact.set_country(self.countrytext.text)

