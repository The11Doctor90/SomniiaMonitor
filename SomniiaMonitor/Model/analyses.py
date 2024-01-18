#  Copyright (c) Matteo Ferreri 2024.
from SomniiaMonitor.Model.doctor import Doctor
from SomniiaMonitor.Model.eeg import Eeg
from SomniiaMonitor.Model.ekg import Ekg
from SomniiaMonitor.Model.inertial import Inertial
from SomniiaMonitor.Model.mask import Mask
from SomniiaMonitor.Model.ppg import Ppg
from SomniiaMonitor.Model.sleeper import Sleeper
from SomniiaMonitor.Model.staging import Staging
from SomniiaMonitor.Model.temperature import Temperature


class Analyses:
    _analyses_id: int
    _start: str
    _end: str
    _sleeper: Sleeper
    _doctor: Doctor
    _mask: Mask
    _ekg: list[Ekg]
    _eeg: list[Eeg]
    _ppg: list[Ppg]
    _staging: list[Staging]
    _inertial: list[Inertial]
    _temp: list[Temperature]

    def __init__(self, analyses_id: int = 0, start: str = "", end: str = "", sleeper: Sleeper = Sleeper(),
                 doctor: Doctor = Doctor(), mask: Mask = Mask()):
        self._analyses_id = analyses_id
        self._start = start
        self._end = end
        self._sleeper = sleeper
        self._doctor = doctor
        self._mask = mask
        self._ekg = []
        self._eeg = []
        self._ppg = []
        self._staging = []
        self._inertial = []
        self._temp = []

    def get_analyses_id(self) -> int:
        return self._analyses_id

    def get_start(self) -> str:
        return self._start

    def get_end(self) -> str:
        return self._end

    def get_sleeper(self) -> Sleeper:
        return self._sleeper

    def get_doctor(self) -> Doctor:
        return self._doctor

    def get_mask(self) -> Mask:
        return self._mask

    def get_ekg(self) -> list[Ekg]:
        return self._ekg

    def get_eeg(self) -> list[Eeg]:
        return self._eeg

    def get_ppg(self) -> list[Ppg]:
        return self._ppg

    def get_staging(self) -> list[Staging]:
        return self._staging

    def get_inertial(self) -> list[Inertial]:
        return self._inertial

    def get_temp(self) -> list[Temperature]:
        return self._temp

    def set_analyses_id(self, analyses_id: int) -> None:
        self._analyses_id = analyses_id

    def set_start(self, start: str) -> None:
        self._start = start

    def set_end(self, end: str) -> None:
        self._end = end

    def set_sleeper(self, sleeper: Sleeper) -> None:
        self._sleeper = sleeper

    def set_doctor(self, doctor: Doctor) -> None:
        self._doctor = doctor

    def set_mask(self, mask: Mask) -> None:
        self._mask = mask

    def add_ekg(self, ekg: Ekg) -> None:
        if ekg not in self._ekg:
            self._ekg.append(ekg)

    def add_eeg(self, eeg: Eeg) -> None:
        if eeg not in self._eeg:
            self._eeg.append(eeg)

    def add_ppg(self, ppg: Ppg) -> None:
        if ppg not in self._ppg:
            self._ppg.append(ppg)

    def add_staging(self, staging: Staging) -> None:
        if staging not in self._staging:
            self._staging.append(staging)

    def add_inertial(self, inertial: Inertial) -> None:
        if inertial not in self._inertial:
            self._inertial.append(inertial)

    def add_temperature(self, temp: Temperature) -> None:
        if temp not in self._temp:
            self._temp.append(temp)
