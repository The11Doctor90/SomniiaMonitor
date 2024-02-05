#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod


class IDbOperation(metaclass=ABCMeta):

    @abstractmethod
    def execute_operation(self):
        raise NotImplementedError
