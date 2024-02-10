#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.user import User


class Doctor(User):
    __doctor_id: int
    __register_code: str
    __fk_contact_id: int | None
    __supervisor_id: int | None

    def __init__(self) -> None:
        super().__init__()
        self.__register_code = ""
        self.__supervisor_id = None
        self.__fk_contact_id = None

    def get_user_id(self) -> int:
        return super().get_user_id()

    def set_user_id(self, user_id: int) -> None:
        super().set_user_id(user_id)

    def get_doctor_id(self) -> int:
        return self.__doctor_id

    def set_doctor_id(self, user_id: int) -> None:
        self.__doctor_id = user_id

    def get_register_code(self) -> str:
        return self.__register_code

    def set_register_code(self, register_code: str) -> None:
        self.__register_code = register_code

    def get_supervisor_id(self) -> int:
        return self.__supervisor_id

    def set_supervisor_id(self, supervisor: int) -> None:
        self.__supervisor_id = supervisor

    def has_empty_field(self) -> bool:
        return super().has_empty_field() or self.__register_code == ""
