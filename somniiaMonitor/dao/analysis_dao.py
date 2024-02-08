#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.analysis import Analysis


class AnalysisDAO(metaclass=ABCMeta):


    @abstractmethod
    def find_all_analyses(self) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analyses_by_sleeper_tax_id(self, tax_id) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analyses_by_doctor_tax_id(self, tax_id) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analyses_by_mask_mac_address(self, mask_mac_address) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analyses_by_code(self, analyses_code):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_analyses(self, analyses: Analysis):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def update_analyses(self, analyses: Analysis):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_analyses(self, analyses: Analysis):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _create_analyses(self, row: tuple):
        raise NotImplementedError("Abstract method")
