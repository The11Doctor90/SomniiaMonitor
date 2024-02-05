#  Copyright (c) Matteo Ferreri 2024.

import sqlite3 as sq
from sqlite3 import Connection, Cursor

from somniiaMonitor.db_interface.interface_db_connection import IDbConnection


class DbConnection(IDbConnection):
    __instance = None
    __connection: Connection | None
    __statement: Cursor | None
    __result_set: Cursor | None
    __row_count: int

    def __init__(self):
        if DbConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__connection = None
            self.__statement = None
            self.__result_set = None
            DbConnection.__instance = self

    @staticmethod
    def get_instance():
        if DbConnection.__instance is None:
            DbConnection()
            try:
                DbConnection.__connection = sq.connect('somniia.db')
            except sq.Error as e:
                print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        return DbConnection.__instance

    @staticmethod
    def execute_query(sql_statement: str) -> Cursor:
        try:
            DbConnection.__statement = DbConnection.__connection.cursor()
            DbConnection.__result_set = DbConnection.__statement.executescript(sql_statement)
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        return DbConnection.__result_set

    @staticmethod
    def execute_update(sql_statement: str) -> int:
        try:
            DbConnection.__statement = DbConnection.__connection.cursor()
            DbConnection.__row_count = DbConnection.__statement.executescript(sql_statement).rowcount
            return DbConnection.__row_count
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        return 0

    @staticmethod
    def close_connection():
        if DbConnection.__result_set is not None:
            try:
                DbConnection.__result_set.close()
            except sq.Error as e:
                print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
            DbConnection.__result_set = None

        if DbConnection.__statement is not None:
            try:
                DbConnection.__statement.close()
            except sq.Error as e:
                print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
            DbConnection.__result_set = None

        if DbConnection.__connection is not None:
            try:
                DbConnection.__connection.close()
            except sq.Error as e:
                print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
            DbConnection.__result_set = None




