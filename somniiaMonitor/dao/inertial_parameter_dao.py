#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.inertial_parameter_composite import InertialParameterComposite
from somniiaMonitor.model.inertial_parameter_data import InertialParameterData


class InertialParameterDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_inertial_parameter_by_analysis_id(self, analysis_id) -> InertialParameterComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_inertial_parameter(self, inertial_parameter: InertialParameterData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_inertial_parameter(self, row: tuple):
        raise NotImplementedError("Abstract method")
