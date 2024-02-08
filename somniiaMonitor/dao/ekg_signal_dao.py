#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.ekg_signal_composite import EkgSignalComposite
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgSignalDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_ekg_signal_by_analysis_code(self, analysis_code) -> EkgSignalComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_ekg_signal(self, ekg_signal: EkgSignalData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_ekg_signal(self, ekg_signal: EkgSignalData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _create_ekg_signal(self, row: tuple):
        raise NotImplementedError("Abstract method")
