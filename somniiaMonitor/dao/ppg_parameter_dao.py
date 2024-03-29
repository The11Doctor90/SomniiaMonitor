#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.ppg_parameter_composite import PpgParameterComposite
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData


class PpgParameterDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_ppg_parameter_by_analysis_id(self, analysis_id) -> PpgParameterComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_ppg_parameter(self, ppg_parameter: PpgParameterData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_ppg_parameter(self, row: tuple):
        raise NotImplementedError("Abstract method")
