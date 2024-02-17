#  Copyright (c) Matteo Ferreri 2024.


class EkgParameterData:
    __ekg_parameter_id: int
    __time: int
    __heart_rate: int
    __heart_rate_variability: int
    __rr_interval: int
    __analysis_id: int

    def __init__(self):
        self.__time = 0
        self.__signal = 0
        self.__heart_rate = 0
        self.__heart_rate_variability = 0
        self.__rr_interval = 0

    def get_ekg_parameter_id(self) -> int:
        return self.__ekg_parameter_id

    def set_ekg_parameter_id(self, ekg_parameter_id: int) -> None:
        self.__ekg_parameter_id = ekg_parameter_id

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

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
