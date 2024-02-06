# Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.ekg_parameter_data import EkgParameterData


class EkgParameterComposite:
    __analysis_code: str
    __ekg_datas: list[EkgParameterData]

    def __init__(self):
        self.__analysis_code = ""
        self.__ekg_datas = []

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def add_ekg_data(self, ekg_data: EkgParameterData) -> None:
        if ekg_data.get_analysis_code() == self.__analysis_code:
            self.__ekg_datas.append(ekg_data)

