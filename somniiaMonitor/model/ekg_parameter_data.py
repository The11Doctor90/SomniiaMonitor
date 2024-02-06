#  Copyright (c) Matteo Ferreri 2024.


class EkgParameterData:
    __analysis_code: str
    __time: int
    __heart_rate: int
    __heart_rate_variability: int
    __rr_interval: int

    def __init__(self):
        self.__analysis_code = ""
        self.__time = 0
        self.__signal = 0
        self.__heart_rate = 0
        self.__heart_rate_variability = 0
        self.__rr_interval = 0

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_ekg_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_heart_rate(self) -> int:
        return self.__heart_rate

    def set_heart_rate(self, heart_rate: int) -> None:
        self.__heart_rate = heart_rate

    def get_heart_rate_variability(self) -> int:
        return self.__heart_rate_variability

    def set_heart_rate_variability(self, heart_rate_variability: int) -> None:
        self.__heart_rate_variability = heart_rate_variability

    def get_rr_interval(self) -> int:
        return self.__rr_interval

    def set_rr_interval(self, rr_interval: int):
        self.__rr_interval = rr_interval
