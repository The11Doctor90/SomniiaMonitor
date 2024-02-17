#  Copyright (c) Matteo Ferreri 2024.


class EegSignalData:
    __eeg_signal_id: int
    __time: int
    __first_channel: int
    __second_channel: int
    __third_channel: int
    __analysis_id: int

    def __init__(self):
        self.__time = 0
        self.__first_channel = 0
        self.__second_channel = 0
        self.__third_channel = 0

    def get_eeg_signal_id(self) -> int:
        return self.__eeg_signal_id

    def set_eeg_signal_id(self, eeg_signal_id: int) -> None:
        self.__eeg_signal_id = eeg_signal_id

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_first_channel(self) -> int:
        return self.__first_channel

    def set_first_channel(self, first_channel: int) -> None:
        self.__first_channel = first_channel

    def get_second_channel(self) -> int:
        return self.__second_channel

    def set_second_channel(self, second_channel: int) -> None:
        self.__second_channel = second_channel

    def get_third_channel(self) -> int:
        return self.__third_channel

    def set_third_channel(self, third_channel: int) -> None:
        self.__third_channel = third_channel
