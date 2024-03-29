#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod

from somniiaMonitor.model.sleeper import Sleeper


class SleeperDAO(metaclass=ABCMeta):


    @abstractmethod
    def find_all_sleepers(self) -> list[Sleeper]:
        raise NotImplementedError("Abstract method")
    @abstractmethod
    def find_sleeper_by_tax_id(self, tax_id):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def add_sleeper(self, sleeper: Sleeper):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def update_sleeper(self, sleeper: Sleeper):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def delete_sleeper(self, sleeper: Sleeper):
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def sleeper_exist_by_tax_id(self, tax_id: str) -> bool:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def sleeper_exist_by_id(self, sleeper_id: int) -> bool:
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def _build_sleeper(self, row: tuple):
        raise NotImplementedError("Abstract method")
