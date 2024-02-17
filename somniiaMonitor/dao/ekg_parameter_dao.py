#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.ekg_parameter_composite import EkgParameterComposite
from somniiaMonitor.model.ekg_parameter_data import EkgParameterData
from somniiaMonitor.model.sleeper import Sleeper


class EkgParameterDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_ekg_parameter_by_analysis_id(self, analysis_id) -> EkgParameterComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_ekg_parameter(self, ekg_parameter: EkgParameterData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_ekg_parameter(self, row: tuple):
        raise NotImplementedError("Abstract method")
