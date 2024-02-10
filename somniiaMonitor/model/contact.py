#  Copyright (c) Matteo Ferreri 2024.


class Contact:
    __contact_id: int
    __email: str
    __phone: str
    __address: str
    __number: str
    __city: str
    __province: str
    __zip_code: str
    __country: str
    __tax_id: str

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

    def get_number(self) -> str:
        return self.__number

    def set_number(self, number: str) -> None:
        self.__number = number

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

    def get_tax_id(self) -> str:
        return self.__tax_id

    def set_tax_id(self, tax_id: str) -> None:
        self.__tax_id = tax_id

    def has_empty_field(self) -> bool:
        return (self.__email == "" or
                self.__phone == "" or
                self.__address == "" or
                self.__city == "" or
                self.__province == "" or
                self.__zip_code == "" or
                self.__country == "" or
                self.__tax_id == "")