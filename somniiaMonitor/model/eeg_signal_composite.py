#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.eeg_signal_data import EegSignalData


class EegSignalComposite:
    __analysis_id: int
    __eeg_datas: list[EegSignalData]

    def __init__(self):
        
        self.__eeg_datas = []

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def add_eeg_data(self, eeg_data: EegSignalData) -> None:
        if eeg_data.get_analysis_id() == self.__analysis_id:
            self.__eeg_datas.append(eeg_data)

