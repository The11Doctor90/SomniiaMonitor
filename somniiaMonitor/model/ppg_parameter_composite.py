#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData


class PpgParameterComposite:
    __analysis_code: str
    __ppg_datas: list[PpgParameterData]

    def __init__(self):
        self.__analysis_code = ""
        self.__ppg_datas = []

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def add_ppg_data(self, ppg_data: PpgParameterData) -> None:
        if ppg_data.get_analysis_code() == self.__analysis_code:
            self.__ppg_datas.append(ppg_data)
