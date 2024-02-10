#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.sleep_stage_data import SleepStageData


class SleepStageComposite:
    __analysis_id: int
    __sleep_stage_datas: list[SleepStageData]

    def __init__(self):
        
        self.__sleep_stage_datas = []

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def add_sleep_stage_data(self, sleep_stage_data: SleepStageData) -> None:
        if sleep_stage_data.get_analysis_id() == self.__analysis_id:
            self.__sleep_stage_datas.append(sleep_stage_data)
