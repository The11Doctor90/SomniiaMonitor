#  Copyright (c) Matteo Ferreri 2024.


class Mask:
    _mask_id: int
    _mac_addr: str
    _name: str

    def __init__(self):
        self._mac_addr = ""
        self._name = ""

    def get_mask_id(self) -> int:
        return self._mask_id

    def set_mask_id(self, mask_id: int):
        self._mask_id = mask_id

    def get_mac_addr(self) -> str:
        return self._mac_addr

    def set_mac_addr(self, mac_addr: str) -> None:
        self._mac_addr = mac_addr

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name
