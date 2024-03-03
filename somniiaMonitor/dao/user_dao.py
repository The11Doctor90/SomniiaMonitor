#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.user import User


class UserDAO(metaclass=ABCMeta):


    @abstractmethod
    def find_all_users(self) -> list[User]:
        raise NotImplementedError("Abstract method")
    @abstractmethod
    def find_user_by_tax_id(self, tax_id):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def update_user(self, user: User):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_user(self, user: User):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def user_exist(self, tax_id):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_user(self, row: tuple):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def check_password(self, email, password):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_user_by_email(self, email):
        raise NotImplementedError("Abstract method")
