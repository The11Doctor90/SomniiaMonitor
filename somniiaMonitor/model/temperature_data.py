#  Copyright (c) Matteo Ferreri 2024.


class TemperatureData:
    __temperature_id: int
    __analysis_id: int
    __time: int
    __temperature: float

    def __init__(self):
        
        self.__time = 0
        self.__temperature = 0

    def get_temperature_id(self) -> int:
        return self.__temperature_id

    def set_temperature_id(self, temperatur_id) -> None:
        self.__temperature_id = temperatur_id

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_temperature(self) -> float:
        return self.__temperature

    def set_temperature(self, temperature: float) -> None:
        self.__temperature = temperature
