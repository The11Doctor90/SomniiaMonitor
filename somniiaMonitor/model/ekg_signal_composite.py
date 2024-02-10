#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgSignalComposite:
    __analysis_id: int
    __ekg_datas: list[EkgSignalData]

    def __init__(self):
        
        self.__ekg_datas = []

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def add_ekg_data(self, ekg_data: EkgSignalData) -> None:
        if ekg_data.get_analysis_id() == self.__analysis_id:
            self.__ekg_datas.append(ekg_data)

