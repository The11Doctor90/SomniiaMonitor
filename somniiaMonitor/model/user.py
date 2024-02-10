#  Copyright (c) Matteo Ferreri 2024.

class User:
    __user_id: int
    __name: str
    __surname: str
    __tax_id: str
    __birth_date: str
    __gender: str
    __created_at: str
    __password: str
    __fk_sleeper_id: int | None
    __fk_doctor_id: int | None
    __fk_contact_id: int | None

    def __init__(self):
        self.__fk_sleeper_id = None
        self.__fk_doctor_id = None
        self.__fk_contact_id = None

    def get_user_id(self) -> int:
        return self.__user_id

    def set_user_id(self, user_id: int) -> None:
        self.__user_id = user_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_surname(self) -> str:
        return self.__surname

    def set_surname(self, surname: str) -> None:
        self.__surname = surname

    def get_birth_date(self) -> str:
        return self.__birth_date

    def set_birth_date(self, birth_date: str) -> None:
        self.__birth_date = birth_date

    def get_tax_id(self) -> str:
        return self.__tax_id

    def set_tax_id(self, tax_id: str) -> None:
        self.__tax_id = tax_id

    def get_gender(self) -> str:
        return self.__gender

    def set_gender(self, gender: str) -> None:
        self.__gender = gender

    def get_created_at(self) -> str:
        return self.__created_at

    def set_created_at(self, created_at: str) -> None:
        self.__created_at = created_at

    def get_sleeper_id(self) -> int:
        return self.__fk_sleeper_id

    def set_sleeper_id(self, sleeper_id: int) -> None:
        self.__fk_sleeper_id = sleeper_id

    def get_doctor_id(self) -> int:
        return self.__fk_doctor_id

    def set_doctor_id(self, doctor_id: int):
        self.__fk_sleeper_id = doctor_id

    def get_contact_id(self) -> int:
        return self.__fk_contact_id

    def set_contact_id(self, contact_id: int) -> None:
        self.__fk_contact_id = contact_id

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str) -> None:
        self.__password = password

    def has_empty_field(self) -> bool:
        return (self.__name == "" or self.__surname == "" or self.__tax_id == ""
                or self.__birth_date == "" or self.__gender == "")
