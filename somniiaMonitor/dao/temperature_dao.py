#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.temperature_composite import TemperatureComposite
from somniiaMonitor.model.temperature_data import TemperatureData


class TemperatureDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_temperature_by_analysis_code(self, analysis_code) -> TemperatureComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_temperature(self, temperature: TemperatureData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_temperature(self, temperature: TemperatureData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _create_temperature(self, row: tuple):
        raise NotImplementedError("Abstract method")
