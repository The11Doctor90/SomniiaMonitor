#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod


class DbOperation(metaclass=ABCMeta):

    @abstractmethod
    def execute_operation(self):
        raise NotImplementedError("Abstract method")
