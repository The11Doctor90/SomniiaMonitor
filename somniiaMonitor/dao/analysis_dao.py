#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.analysis import Analysis


class AnalysisDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_all_analyses(self) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analyses_by_sleeper_id(self, sleeper_id) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analyses_by_doctor_id(self, doctor_id) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analyses_by_mask_id(self, mask_id) -> list[Analysis]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analysis_by_id(self, analyses_id):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_analysis_by_code(self, analyses_code: str):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_analysis(self, analysis: Analysis):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def update_analysis(self, analysis: Analysis):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_analysis(self, analyses: Analysis):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_analyses(self, row: tuple):
        raise NotImplementedError("Abstract method")
