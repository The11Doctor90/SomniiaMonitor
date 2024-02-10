#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.temperature_data import TemperatureData


class TemperatureComposite:
    __analysis_id: int
    __temperature_datas: list[TemperatureData]

    def __init__(self):
        
        self.__temperature_datas = []

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def add_temperature_data(self, temperature_data: TemperatureData) -> None:
        if temperature_data.get_analysis_id() == self.__analysis_id:
            self.__temperature_datas.append(temperature_data)

