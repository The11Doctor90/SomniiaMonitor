#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.temperature_data import TemperatureData


class TemperatureComposite:
    __analysis_code: str
    __temperature_datas: list[TemperatureData]

    def __init__(self):
        self.__analysis_code = ""
        self.__temperature_datas = []

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def add_temperature_data(self, temperature_data: TemperatureData) -> None:
        if temperature_data.get_analysis_code() == self.__analysis_code:
            self.__temperature_datas.append(temperature_data)

