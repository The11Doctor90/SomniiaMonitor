#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.ekg_signal_composite import EkgSignalComposite
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgSignalDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_ekg_signal_by_analysis_id(self, analysis_id) -> EkgSignalComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_ekg_signal(self, ekg_signal: EkgSignalData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_ekg_signal(self, row: tuple):
        raise NotImplementedError("Abstract method")
