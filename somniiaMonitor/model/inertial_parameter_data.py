#  Copyright (c) Matteo Ferreri 2024.


class InertialParameterData:
    __inertial_parameter_id: int
    __time: int
    __root_mean_square: float
    __roll: float
    __pitch: float
    __yaw: float
    __analysis_id: int

    def __init__(self):
        self.__time = 0
        self.__root_mean_square = 0.0
        self.__roll = 0.0
        self.__pitch = 0.0
        self.__yaw = 0.0

    def get_inertial_parameter_id(self) -> int:
        return self.__inertial_parameter_id

    def set_inertial_parameter_id(self, inertial_parameter_id: int) -> None:
        self.__inertial_parameter_id = inertial_parameter_id

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def get_time(self) -> int:
        return self.__time

    def set_time(self, time: int) -> None:
        self.__time = time

    def get_root_mean_square(self) -> float:
        return self.__root_mean_square

    def set_root_mean_square(self, value: float) -> None:
        self.__root_mean_square = value

    def get_roll(self) -> float:
        return self.__roll

    def set_roll(self, roll: float) -> None:
        self.__roll = roll

    def get_pitch(self) -> float:
        return self.__pitch

    def set_pitch(self, pitch: float) -> None:
        self.__pitch = pitch

    def get_yaw(self) -> float:
        return self.__yaw

    def set_yaw(self, yaw: float) -> None:
        self.__yaw = yaw
