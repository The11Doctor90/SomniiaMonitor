#  Copyright (c) Matteo Ferreri 2024.
from SomniiaMonitor.Model.doctor import Doctor
from SomniiaMonitor.Model.mask import Mask
from SomniiaMonitor.Model.sleeper import Sleeper


class Analyses:
    _start: str
    _end: str
    _sleeper: Sleeper
    _doctor: Doctor
    _mask: Mask
    _ekg: Ekg
    _eeg: Eeg
    _ppg: Ppg
    _staging: Staging
    _inertial: Inertial
    _temp: Temperature

