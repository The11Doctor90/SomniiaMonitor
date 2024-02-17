#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData


class PpgParameterComposite:
    __analysis_id: int
    __ppg_datas: list[PpgParameterData]

    def __init__(self):
        
        self.__ppg_datas = []

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def add_ppg_data(self, ppg_data: PpgParameterData) -> None:
        if ppg_data.get_analysis_id() == self.__analysis_id:
            self.__ppg_datas.append(ppg_data)
