#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.eeg_signal_composite import EegSignalComposite
from somniiaMonitor.model.eeg_signal_data import EegSignalData


class EegSignalDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_eeg_signal_by_analysis_code(self, analysis_code) -> EegSignalComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_eeg_signal(self, eeg_signal: EegSignalData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_eeg_signal(self, eeg_signal: EegSignalData):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _create_eeg_signal(self, row: tuple):
        raise NotImplementedError("Abstract method")
