#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.supervisor import Supervisor
from somniiaMonitor.model.user import User


class Doctor(User):
    __register_code: str
    __contact: Contact | None
    __supervisor: Supervisor | None

    def __init__(self) -> None:
        super().__init__()
        self.__register_code = ""
        self.__supervisor = None

    def get_register_code(self) -> str:
        return self.__register_code

    def set_register_code(self, register_code: str) -> None:
        self.__register_code = register_code

    def get_supervisor(self) -> Supervisor:
        return self.__supervisor

    def set_supervisor(self, supervisor: Supervisor) -> None:
        self.__supervisor = supervisor


