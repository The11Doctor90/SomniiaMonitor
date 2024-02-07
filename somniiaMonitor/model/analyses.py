#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.doctor import Doctor
from somniiaMonitor.model.eeg_signal_composite import EegSignalComposite
from somniiaMonitor.model.ekg_parameter_composite import EkgParameterComposite
from somniiaMonitor.model.ekg_signal_composite import EkgSignalComposite
from somniiaMonitor.model.inertial_parameter_composite import InertialParameterComposite
from somniiaMonitor.model.mask import Mask
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData
from somniiaMonitor.model.sleep_stage_composite import SleepStageComposite
from somniiaMonitor.model.sleeper import Sleeper
from somniiaMonitor.model.temperature_composite import TemperatureComposite


class Analyses:
    __analysis_id: int
    __start: str
    __end: str
    __sleeper: Sleeper | None
    __doctor: Doctor | None
    __mask: Mask | None
    __code: str
    __ekg_signal_data: EkgSignalComposite | None
    __ekg_parameter_data: EkgParameterComposite | None
    __eeg_signal_data: EegSignalComposite | None
    __ppg_parameter_data: PpgParameterData | None
    __sleep_stage_data: SleepStageComposite | None
    __inertial_parameter_data: InertialParameterComposite | None
    __temperature_data: TemperatureComposite | None

    def __init__(self):
        self.__start = ""
        self.__sleeper = None
        self.__doctor = None
        self.__mask = None
        self.__ekg_signal_data = None
        self.__ekg_parameter_data = None
        self.__eeg_signal_data = None
        self.__ppg_parameter_data = None
        self.__sleep_stage_data = None
        self.__inertial_parameter_data = None
        self.__temperature_data = None

    def get_analysis_id(self) -> int:
        return self.__analysis_id

    def set_analysis_id(self, analysis_id: int) -> None:
        self.__analysis_id = analysis_id

    def get_start(self) -> str:
        return self.__start

    def set_start(self, start: str) -> None:
        self.__start = start

    def get_end(self) -> str:
        return self.__end

    def set_end(self, end: str) -> None:
        self.__end = end

    def get_sleeper(self) -> Sleeper:
        return self.__sleeper

    def set_sleeper(self, sleeper: Sleeper) -> None:
        self.__sleeper = sleeper

    def get_doctor(self) -> Doctor:
        return self.__doctor

    def set_doctor(self, doctor: Doctor) -> None:
        self.__doctor = doctor

    def get_mask(self) -> Mask:
        return self.__mask

    def set_mask(self, mask: Mask) -> None:
        self.__mask = mask

    def get_code(self) -> str:
        return self.__code

    def set_code(self, code: str) -> None:
        self.__code = code

    def get_ekg_signal_data(self) -> EkgSignalComposite:
        return self.__ekg_signal_data

    def set_ekg_signal_data(self, ekg_signal_data: EkgSignalComposite) -> None:
        self.__ekg_signal_data = ekg_signal_data

    def get_ekg_parameter_data(self) -> EkgParameterComposite:
        return self.__ekg_parameter_data

    def set_ekg_parameter_data(self, ekg_parameter_data: EkgParameterComposite) -> None:
        self.__ekg_parameter_data = ekg_parameter_data

    def get_eeg_signal_data(self) -> EegSignalComposite:
        return self.__eeg_signal_data

    def set_eeg_signal_data(self, eeg_signal_data: EegSignalComposite) -> None:
        self.__eeg_signal_data = eeg_signal_data

    def get_ppg_parameter_data(self) -> PpgParameterData:
        return self.__ppg_parameter_data

    def set_ppg_parameter_data(self, ppg_parameter_data: PpgParameterData) -> None:
        self.__ppg_parameter_data = ppg_parameter_data

    def get_sleep_stage_data(self) -> SleepStageComposite:
        return self.__sleep_stage_data

    def set_sleep_stage_data(self, sleep_stage_data: SleepStageComposite) -> None:
        self.__sleep_stage_data = sleep_stage_data

    def get_inertial_parameter_data(self) -> InertialParameterComposite:
        return self.__inertial_parameter_data

    def set_inertial_parameter_data(self, inertial_parameter_data: InertialParameterComposite) -> None:
        self.__inertial_parameter_data = inertial_parameter_data

    def get_temperature_data(self) -> TemperatureComposite:
        return self.__temperature_data

    def set_temperature_data(self, temperature_data: TemperatureComposite) -> None:
        self.__temperature_data = temperature_data

