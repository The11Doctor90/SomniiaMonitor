#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.inertial_parameter_data import InertialParameterData


class InertialParameterComposite:
    __analysis_code: str
    __inertial_datas: list[InertialParameterData]

    def __init__(self):
        self.__analysis_code = ""
        self.__inertial_datas = []

    def get_analysis_code(self) -> str:
        return self.__analysis_code

    def set_analysis_code(self, analysis_code: str) -> None:
        self.__analysis_code = analysis_code

    def add_ekg_data(self, inertial_data: InertialParameterData) -> None:
        if inertial_data.get_analysis_code() == self.__analysis_code:
            self.__inertial_datas.append(inertial_data)

