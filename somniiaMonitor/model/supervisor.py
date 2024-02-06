#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.doctor import Doctor


class Supervisor:
    __doctor: Doctor | None

    def __init__(self):
        self.__doctor = None

    def get_doctor(self) -> Doctor:
        return self.__doctor

    def set_doctor(self, doctor: Doctor) -> None:
        self.__doctor = doctor

