#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.user import User


class Doctor(User):
    __register_code: str
    __contact: Contact | None
    __supervisor_id: str

    def __init__(self) -> None:
        super().__init__()
        self.__register_code = ""
        self.__supervisor_id = ""

    def get_register_code(self) -> str:
        return self.__register_code

    def set_register_code(self, register_code: str) -> None:
        self.__register_code = register_code

    def get_supervisor_id(self) -> str:
        return self.__supervisor_id

    def set_supervisor_id(self, supervisor: str) -> None:
        self.__supervisor_id = supervisor


