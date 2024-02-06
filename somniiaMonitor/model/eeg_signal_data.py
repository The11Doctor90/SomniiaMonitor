#  Copyright (c) Matteo Ferreri 2024.


class EegSignalData:
    __analysis_code: str
    __time: int
    __channel_1: int
    __channel_2: int
    __channel_3: int

    def __init__(self):
        self.__analysis_code = ""
        self.__time = 0
        self.__channel_1 = 0
        self.__channel_2 = 0
        self.__channel_3 = 0

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_ekg_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_channel_1(self) -> int:
        return self.__channel_1

    def set_channel_1(self, channel_1: int) -> None:
        self.__channel_1 = channel_1

    def get_channel_2(self) -> int:
        return self.__channel_2

    def set_channel_2(self, channel_2: int) -> None:
        self.__channel_2 = channel_2

    def get_channel_3(self) -> int:
        return self.__channel_3

    def set_channel_3(self, channel_3: int) -> None:
        self.__channel_3 = channel_3
