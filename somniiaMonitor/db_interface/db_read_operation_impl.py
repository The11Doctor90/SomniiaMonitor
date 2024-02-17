#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_operation import DbOperation


class DbReadOperationImpl(DbOperation):
    __connection: DbConnectionImpl
    __sql: str

    def __init__(self, sql: str):
        self.__connection = DbConnectionImpl.get_instance()
        self.__sql = sql

    def execute_operation(self):
        return self.__connection.execute_query(self.__sql)
