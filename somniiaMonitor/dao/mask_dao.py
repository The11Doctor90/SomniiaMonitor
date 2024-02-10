#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.mask import Mask


class MaskDAO(metaclass=ABCMeta):

    @abstractmethod
    def find_all_masks(self) -> list[Mask]:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def find_mask_by_mac_address(self, mac_addr):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_mask(self, mask: Mask):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def update_mask(self, mask: Mask):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_mask(self, mask: Mask):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def mask_exist(self, mask_addr) -> bool:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_mask(self, row: tuple):
        raise NotImplementedError("Abstract method")
