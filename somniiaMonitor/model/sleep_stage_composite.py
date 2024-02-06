#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.sleep_stage_data import SleepStageData

class EkgSignalComposite:
    __analysis_code: str
    __sleep_stage_datas: list[SleepStageData]

    def __init__(self):
        self.__analysis_code = ""
        self.__sleep_stage_datas = []

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def add_sleep_stage_data(self, sleep_stage_data: SleepStageData) -> None:
        if sleep_stage_data.get_analysis_code() == self.__analysis_code:
            self.__sleep_stage_datas.append(sleep_stage_data)

