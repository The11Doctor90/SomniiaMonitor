#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.inertial_parameter_data import InertialParameterData


class InertialParameterComposite:
    __analysis_id: int
    __inertial_datas: list[InertialParameterData]

    def __init__(self):
        
        self.__inertial_datas = []

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def add_inertial_data(self, inertial_data: InertialParameterData) -> None:
        if inertial_data.get_analysis_id() == self.__analysis_id:
            self.__inertial_datas.append(inertial_data)

