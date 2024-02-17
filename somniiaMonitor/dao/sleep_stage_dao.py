#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.sleep_stage_composite import SleepStageComposite
from somniiaMonitor.model.sleep_stage_data import SleepStageData


class SleepStageDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_sleep_stage_by_analysis_id(self, analysis_id) -> SleepStageComposite:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_sleep_stage(self, sleep_stage: SleepStageData):
        raise NotImplementedError("Abstract method")


    @abstractmethod
    def _build_sleep_stage(self, row: tuple):
        raise NotImplementedError("Abstract method")
