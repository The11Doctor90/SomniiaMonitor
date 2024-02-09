#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.user import User


class Doctor(User):
    __doctor_id: int
    __user_id: int
    __register_code: str
    __contact: Contact | None
    __supervisor_id: int | None

    def __init__(self) -> None:
        super().__init__()
        self.__register_code = ""
        self.__supervisor_id = None
        self.__contact = None

    def get_register_code(self) -> str:
        return self.__register_code

    def set_register_code(self, register_code: str) -> None:
        self.__register_code = register_code

    def get_supervisor_id(self) -> int:
        return self.__supervisor_id

    def set_supervisor_id(self, supervisor: int) -> None:
        self.__supervisor_id = supervisor


