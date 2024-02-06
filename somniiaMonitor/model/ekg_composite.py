#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgComposite:
    __analyses_id: int
    __ekg_data: list[EkgSignalData]

    def __init__(self, analyses_id: int):
        self.__analyses_id = analyses_id