#  Copyright (c) Matteo Ferreri 2024.


class SleepStageData:
    __sleep_stage_id: int
    __analysis_code: str
    __time: int
    __stage: str

    def __init__(self):
        self.__analysis_code = ""
        self.__time = 0
        self.__stage = ""

    def get_sleep_stage_id(self) -> int:
        return self.__sleep_stage_id

    def set_sleep_stage_id(self, sleep_stage_id: int) -> None:
        self.__sleep_stage_id = sleep_stage_id

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_stage(self) -> str:
        return self.__stage

    def set_stage(self, stage: str) -> None:
        self.__stage = stage
