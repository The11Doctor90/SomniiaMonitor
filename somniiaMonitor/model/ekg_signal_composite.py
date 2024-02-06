#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgSignalComposite:
    __analysis_code: str
    __ekg_datas: list[EkgSignalData]

    def __init__(self):
        self.__analysis_code = ""
        self.__ekg_datas = []

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def add_ekg_data(self, ekg_data: EkgSignalData) -> None:
        if ekg_data.get_analysis_code() == self.__analysis_code:
            self.__ekg_datas.append(ekg_data)

