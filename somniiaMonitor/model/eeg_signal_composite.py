#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.eeg_signal_data import EegSignalData


class EegSignalComposite:
    __analysis_code: str
    __eeg_datas: list[EegSignalData]

    def __init__(self):
        self.__analysis_code = ""
        self.__eeg_datas = []

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def add_eeg_data(self, eeg_data: EegSignalData) -> None:
        if eeg_data.get_analysis_code() == self.__analysis_code:
            self.__eeg_datas.append(eeg_data)

