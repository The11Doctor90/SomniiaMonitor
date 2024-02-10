#  Copyright (c) Matteo Ferreri 2024.

import sqlite3 as sq
from sqlite3 import Connection, Cursor

from somniiaMonitor.db_interface.db_connection import DbConnection

class DbConnectionImpl(DbConnection):
    __instance = None
    __connection: Connection | None
    __cursor: Cursor | None
    __result_set: Cursor | None
    __row_count: int

    def __init__(self):
        print(f"init: {DbConnectionImpl.__instance}")
        if DbConnectionImpl.__instance is not None:
            raise RuntimeError("This class is a singleton!")
        else:
            self.__connection = None
            self.__cursor = None
            DbConnectionImpl.__instance = self

    @staticmethod
    def get_instance():
        if DbConnectionImpl.__instance is None:
            DbConnectionImpl()
        try:
            DbConnectionImpl.__connection = sq.connect('database/somniia.db')
            DbConnectionImpl.__connection.execute("PRAGMA foreign_keys = ON;")
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        return DbConnectionImpl.__instance

    @staticmethod
    def execute_query(sql_statement: str) -> Cursor:
        try:
            DbConnectionImpl.__cursor = DbConnectionImpl.__connection.cursor()
            DbConnectionImpl.__result_set = DbConnectionImpl.__cursor.execute(sql_statement)
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        return DbConnectionImpl.__result_set

    @staticmethod
    def execute_update(sql_statement: str) -> int:
        try:
            DbConnectionImpl.__cursor = DbConnectionImpl.__connection.cursor()
            DbConnectionImpl.__row_count = DbConnectionImpl.__cursor.execute(sql_statement).rowcount

            DbConnectionImpl.__connection.commit()
            return DbConnectionImpl.__row_count
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        return 0

    @staticmethod
    def close_connection():
        DbConnectionImpl.__result_set = None

        if DbConnectionImpl.__cursor is not None:
            try:
                DbConnectionImpl.__cursor.close()
            except sq.Error as e:
                print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")

        if DbConnectionImpl.__connection is not None:
            try:
                DbConnectionImpl.__connection.close()
            except sq.Error as e:
                print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
