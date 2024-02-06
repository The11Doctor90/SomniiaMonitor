#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.supervisor import Supervisor
from somniiaMonitor.model.user import User


class Doctor(User):
    __user_id: int
    __name: str
    __surname: str
    __tax_id: str
    __birthday: int
    __birthmonth: int
    __birthyear: int
    __gender: str
    __created_at: str
    __register_code: str
    __contact: Contact | None
    __supervisor: Supervisor | None
    __analyses = list[Analyses]

    def __init__(self) -> None:
        self.__name = ""
        self.__surname = ""
        self.__tax_id = ""
        self.__gender = ""
        self.__created_at = ""
        self.__register_code = ""
        self.__supervisor = None
        self.__analyses = []

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

    def get_birthday(self) -> int:
        return self.__birthday

    def set_birthday(self, birthday: int) -> None:
        self.__birthday = birthday

    def get_birthmonth(self) -> int:
        return self.__birthmonth

    def set_birthmonth(self, birthmonth: int) -> None:
        self.__birthmonth = birthmonth

    def get_birthyear(self) -> int:
        return self.__birthyear

    def set_birthyear(self, birthyear: int) -> None:
        self.__birthyear = birthyear

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

    def get_register_code(self) -> str:
        return self.__register_code

    def set_register_code(self, register_code: str) -> None:
        self.__register_code = register_code

    def get_supervisor(self) -> Supervisor:
        return self.__supervisor

    def set_supervisor(self, supervisor: Supervisor) -> None:
        self.__supervisor = supervisor

    def get_contact(self) -> Contact:
        return self.__contact

    def set_contact(self, contact: Contact) -> None:
        self.__contact = contact

    def get_analyses_list(self) -> list[Analyses]:
        return self.__analyses

    def add_analyses(self, analyses: Analyses) -> None:
        self.__analyses.append(analyses)

    def remove_analyses(self, analyses: Analyses) -> None:
        self.__analyses.remove(analyses)

    def clear_analyses_list(self) -> None:
        self.__analyses = []

    def add_analyses_list(self, analyses_list: list[Analyses]) -> None:
        if len(analyses_list) > 0:
            for analyses in analyses_list:
                if analyses not in self.__analyses:
                    self.__analyses.append(analyses)

