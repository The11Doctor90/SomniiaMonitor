#  Copyright (c) Matteo Ferreri 2024.


class Contact:
    __contact_id: int
    __email: str
    __phone: str
    __address: str
    __number: int
    __city: str
    __province: str
    __zip_code: str
    __country: str

    def __init__(self):
        self.__email = ""
        self.__phone = ""
        self.__address = ""
        self.__city = ""
        self.__province = ""
        self.__zip_code = ""
        self.__country = ""

    def get_contact_id(self) -> int:
        return self.__contact_id

    def set_contact_id(self, contact_id: int) -> None:
        self.__contact_id = contact_id

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_phone(self) -> str:
        return self.__phone

    def set_phone(self, phone: str) -> None:
        self.__phone = phone

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str) -> None:
        self.__address = address

    def get_city(self) -> str:
        return self.__city

    def set_city(self, city: str) -> None:
        self.__city = city

    def get_province(self) -> str:
        return self.__province

    def set_province(self, province: str) -> None:
        self.__province = province

    def get_zip_code(self) -> str:
        return self.__zip_code

    def set_zip_code(self, zip_code: str) -> None:
        self.__zip_code = zip_code

    def get_country(self) -> str:
        return self.__country

    def set_country(self, country: str) -> None:
        self.__country = country
