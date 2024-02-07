#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.contact import Contact


class ContactDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_all_contacts(self) -> list[Contact]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_contact_by_tax_id(self, tax_id: str) -> Contact:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_contact_by_email(self, email: str) -> Contact:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_user_by_phone(self, phone: str) -> Contact:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_contact(self, contact: Contact):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def update_contactr(self, contact: Contact):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_contact(self, contact: Contact):
        raise NotImplementedError("Abstract method")
