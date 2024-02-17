#  Copyright (c) Matteo Ferreri 2024.


class Mask:
    __mask_id: int
    __mac_addr: str
    __name: str
    __status: str

    def __init__(self):
        self.__status = ""

    def get_mask_id(self) -> int:
        return self.__mask_id

    def set_mask_id(self, mask_id: int) -> None:
        self.__mask_id = mask_id

    def get_mac_addr(self) -> str:
        return self.__mac_addr

    def set_mac_addr(self, mac_addr: str) -> None:
        self.__mac_addr = mac_addr

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_status(self) -> str:
        return self.__status

    def set_status(self, status: str) -> None:
        self.__status = status
