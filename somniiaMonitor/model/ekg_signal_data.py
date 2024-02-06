#  Copyright (c) Matteo Ferreri 2024.


class EkgSignalData:
    __ekg_signal_data_id: int
    __time: int
    __signal: int

    def __init__(self):
        self.__ekg_signal_data_id = 0
        self.__time = 0
        self.__signal = 0

    def get_ekg_signal_data_id(self) -> int:
        return self.__ekg_signal_data_id

    def set_ekg_signal_data_id(self, id: str) -> None:
        self.__ekg_signal_data_id = id

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = int

    def get_signal(self, signal: int) -> int:
        return self.__signal

    def set_signal(self, signal: int) -> None:
        self.__signal = signal