#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.doctor import Doctor
from somniiaMonitor.model.mask import Mask
from somniiaMonitor.model.sleeper import Sleeper


class Analyses:
    __start: str
    __end: str
    __sleeper: Sleeper | None
    __doctor: Doctor | None
    __mask: Mask | None
    __code: str
    # _ekg: Ekg
    # _eeg: Eeg
    # _ppg: Ppg
    # _staging: Staging
    # _inertial: Inertial
    # _temp: Temperature

    def __init__(self):
        self.__start = ""
        self.__sleeper = None
        self.__doctor = None
        self.__mask = None

    def get_start(self) -> str:
        return self.__start

    def set_start(self, start: str) -> None:
        self.__start = start

    def get_end(self) -> str:
        return self.__end

    def set_end(self, end: str) -> None:
        self.__end = end

    def get_sleeper(self) -> Sleeper:
        return self.__sleeper

    def set_sleeper(self, sleeper: Sleeper) -> None:
        self.__sleeper = sleeper

    def get_doctor(self) -> Doctor:
        return self.__doctor

    def set_doctor(self, doctor: Doctor) -> None:
        self.__doctor = doctor

    def get_mask(self) -> Mask:
        return self.__mask

    def set_mask(self, mask: Mask) -> None:
        self.__mask = mask

    def get_code(self) -> str:
        return self.__code

    def set_code(self, code: str) -> None:
        self.__code = code
