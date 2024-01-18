#  Copyright (c) Matteo Ferreri 2024.


class Mask:
    _mask_id: int
    _mac_addr: str
    _name: str
    _uuid_service: str
    _uuid_rx: str
    _uuid_tx: str

    def __init__(self, mask_id, mac_addr: str = "", name: str = "", uuid_service: str = "", uuid_rx: str = "", uuid_tx: str = ""):
        self._mask_id = mask_id
        self._mac_addr = mac_addr
        self._name = name
        self._uuid_service = uuid_service
        self._uuid_rx = uuid_rx
        self._uuid_tx = uuid_tx

    def get_mac_addr(self) -> str:
        return self._mac_addr

    def get_name(self) -> str:
        return self._name

    def get_uuid_service(self) -> str:
        return self._uuid_service

    def get_uuid_rx(self) -> str:
        return self._uuid_rx

    def get_uuid_tx(self) -> str:
        return self._uuid_tx

    def set_mac_addr(self, mac_addr: str) -> None:
        self._mac_addr = mac_addr

    def set_name(self, name: str) -> None:
        self._name = name

    def set_uuid_service(self, uuid_service: str) -> None:
        self._uuid_service = uuid_service

    def set_uuid_rx(self, uuid_rx: str) -> None:
        self._uuid_rx = uuid_rx

    def set_uuid_tx(self, uuid_tx: str) -> None:
        self._uuid_tx = uuid_tx