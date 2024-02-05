#  Copyright (c) Matteo Ferreri 2024.

from abc import ABCMeta, abstractmethod


class IDbConnection(metaclass=ABCMeta):
    """Class that takes care of the connection to the database."""

    @staticmethod
    @abstractmethod
    def execute_query(sql_statement: str):
        """ It takes as input a string containing an SQL query and executes it.
            @param sql_statement: String containing an SQL query to execute.
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def execute_update(sql_statement: str) -> int:
        """ It takes as input a string containing a modification SQL query and executes it.
            @param sql_statement: String containing a change SQL query to execute.
            @return: The number of rows affected
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def close_connection():
        """Close the db connection"""
        raise NotImplementedError
