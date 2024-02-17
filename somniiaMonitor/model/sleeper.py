#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.user import User


class Sleeper(User):
    __sleeper_id: int


    def __init__(self):
        super().__init__()

    def get_user_id(self) -> int:
        return super().get_user_id()

    def set_user_id(self, user_id: int) -> None:
        super().set_user_id(user_id)

    def get_sleeper_id(self) -> int:
        return self.__sleeper_id

    def set_sleeper_id(self, sleeper_id: int) -> None:
        self.__sleeper_id = sleeper_id

    def has_empty_field(self) -> bool:
        return super().has_empty_field()


