#  Copyright (c) Matteo Ferreri 2024.


class PpgParameterData:
    __ppg_parameter_id: int
    __analysis_code: str
    __time: int
    __heart_rate: int
    __spo2: int
    __perfusion_index: float
    __breath_frequency: int

    def __init__(self):
        self.__analysis_code = ""
        self.__time = 0
        self.__heart_rate = 0
        self.__spo2 = 0
        self.__perfusion_index = 0.0
        self.__breath_frequency = 0

    def get_ppg_parameter_id(self) -> int:
        return self.__ppg_parameter_id

    def set_ppg_parameter_id(self, ppg_parameter_id: int) -> None:
        self.__ppg_parameter_id = ppg_parameter_id

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_heart_rate(self) -> int:
        return self.__heart_rate

    def set_heart_rate(self, heart_rate: int) -> None:
        self.__heart_rate = heart_rate

    def get_spo2(self) -> int:
        return self.__spo2

    def set_spo2(self, spo2: int) -> None:
        self.__spo2 = spo2

    def get_perfusion_index(self) -> float:
        return self.__perfusion_index

    def set_perfusion_index(self, perfusion_index: float) -> None:
        self.__perfusion_index = perfusion_index

    def get_breath_frequency(self) -> int:
        return self.__breath_frequency

    def set_breath_frequency(self, breath_frequency: int) -> None:
        self.__breath_frequency = breath_frequency
