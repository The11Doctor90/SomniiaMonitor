#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.db_interface.interface_db_operation import IDbOperation


class DbUpdateOperation(IDbOperation):
    __connection: DbConnection
    __sql: str

    def __init__(self, sql: str):
        self.__connection = DbConnection.get_instance()
        self.__sql = sql

    def execute_operation(self) -> int:
        return self.__connection.execute_update(self.__sql)