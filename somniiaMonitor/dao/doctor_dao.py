#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.doctor import Doctor


class DoctorDAO(metaclass=ABCMeta):


    @abstractmethod
    def find_all_doctor(self) -> list[Doctor]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_all_doctor_by_supervisor_tax_id(self, supervisor_tax_id) -> list[Doctor]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_doctor_by_tax_id(self, tax_id):
        raise NotImplementedError("Abstract method")


    @abstractmethod
    def add_doctor(self, doctor: Doctor):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def update_doctor(self, doctor: Doctor):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_doctor(self, doctor: Doctor):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _create_doctor(self, row: tuple):
        raise NotImplementedError("Abstract method")
