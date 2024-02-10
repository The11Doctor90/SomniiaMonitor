#  Copyright (c) Matteo Ferreri 2024.


class EkgSignalData:
    __ekg_signal_id: int
    __time: int
    __signal: int
    __analysis_id: int

    def __init__(self):
        self.__time = 0
        self.__signal = 0

    def get_ekg_signal_id(self) -> int:
        return self.__ekg_signal_id

    def set_ekg_signal_id(self, ekg_signal_id: int) -> None:
        self.__ekg_signal_id = ekg_signal_id

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_signal(self) -> int:
        return self.__signal

    def set_signal(self, signal: int) -> None:
        self.__signal = signal
