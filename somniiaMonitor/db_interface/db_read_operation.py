#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.db_interface.interface_db_operation import IDbOperation


class DbReadOperation(IDbOperation):
    __connection: DbConnection
    __sql: str

    def __init__(self, sql: str):
        self.__connection = DbConnection.get_instance()
        self.__sql = sql

    def execute_operation(self):
        return self.__connection.execute_query(self.__sql)