#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod


class DbConnection(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def execute_query(sql_statement: str):
        raise NotImplementedError("Abstract method")

    @staticmethod
    @abstractmethod
    def execute_update(sql_statement: str) -> int:
        raise NotImplementedError("Abstract method")

    @staticmethod
    @abstractmethod
    def close_connection():
        raise NotImplementedError("Abstract method")
