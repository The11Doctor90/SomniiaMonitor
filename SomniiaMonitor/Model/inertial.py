#  Copyright (c) Matteo Ferreri 2024.


class Inertial:
    _inertial_id: int
    _rms: float
    _roll: float
    _pitch: float
    _yaw: float

    def __init__(self, inertial_id: int = 0, rms: float = 0, roll: float = 0, pitch: float = 0, yaw: float = 0):
        self._inertial_id = inertial_id
        self._rms = rms
        self._roll = roll
        self._pitch = pitch
        self._yaw = yaw

    def get_inertial_id(self) -> int:
        return self._inertial_id

    def get_rms(self) -> float:
        return self._rms

    def get_roll(self) -> float:
        return self._roll

    def get_pitch(self) -> float:
        return self._pitch

    def get_yaw(self) -> float:
        return self._yaw

    def set_inertial_id(self, inertial_id: int) -> None:
        self._inertial_id = inertial_id

    def set_rms(self, rms: float) -> None:
        self._rms = rms

    def set_roll(self, roll: float) -> None:
        self._roll = roll

    def set_pitch(self, pitch: float) -> None:
        self._pitch = pitch

    def set_yaw(self, yaw: float) -> None:
        self._yaw = yaw