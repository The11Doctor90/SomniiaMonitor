#  Copyright (c) Matteo Ferreri 2024.
from abc import abstractmethod, ABCMeta

from somniiaMonitor.model.contact import Contact


class User(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def set_name(self, name: str) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_surname(self) -> str:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def set_surname(self, surname: str) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_birthday(self) -> int:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def set_birthday(self, birthday: int) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_birthmonth(self) -> int:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def set_birthmonth(self, birthmonth: int) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_birthyear(self) -> int:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def set_birthyear(self, birthyear: int) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_tax_id(self) -> str:
        raise NotImplementedError(f"Abstract method")

    @abstractmethod
    def set_tax_id(self, tax_id: str) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_gender(self) -> str:
        raise NotImplementedError(f"Abstract method")

    @abstractmethod
    def set_gender(self, gender: str) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_created_at(self) -> str:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def set_created_at(self, created_at: str) -> None:
        raise NotImplementedError(f"Abstract method")

    @abstractmethod
    def get_contact(self) -> Contact:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def set_contact(self, contact: Contact) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def get_analyses_list(self) -> list[Analyses]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_analyses(self, analyses: Analyses) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def remove_analyses(self, analyses: Analyses) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def clear_analyses_list(self) -> None:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_analyses_list(self, analyses_list: list[Analyses]) -> None:
        raise NotImplementedError("Abstract method")