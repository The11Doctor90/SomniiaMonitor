#  Copyright (c) Matteo Ferreri 2024.


class Temperature:
    _temp_id: int
    _time: str
    _temperature: float

    def __init__(self, temp_id: int = 0, time: str = "", temperature: float = 0):
        self._temp_id = temp_id
        self._time = time
        self._temperature = temperature

    def get_id(self) -> int:
        return self._temp_id

    def get_time(self) -> str:
        return self._time

    def get_temperature(self) -> float:
        return self._temperature

    def set_id(self, temp_id: int) -> None:
        self._temp_id = temp_id

    def set_time(self, time: str) -> None:
        self._time = time

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
