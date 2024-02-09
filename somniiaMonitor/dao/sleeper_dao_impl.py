#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.sleeper_dao import SleeperDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.sleeper import Sleeper


class SleeperDAOImpl(SleeperDAO):
    __USER_ID, __NAME, __SURNAME, __TAX_ID, __BIRTHDATE, __GENDER, __CREATE_AT = 0, 1, 2, 3, 4, 5, 6
    __ROW_ALONE = 0
    __instance = None
    __sleeper: Sleeper | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if SleeperDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__sleeper = None
            self.__connection = None
            self.__result_set = None
            SleeperDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if SleeperDAOImpl.__instance is None:
            SleeperDAOImpl()
        return SleeperDAOImpl.__instance

    def find_all_sleepers(self) -> list[Sleeper] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT user_id, name, surname, tax_id, birth_date, gender, created_at FROM sleepers d INNER JOIN users u on u.tax_id = d.sleeper_tax_id"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        sleepers = []
        try:
            for row in self.__result_set.fetchall():
                print(row)
                self._create_sleeper(row)
                sleepers.append(self.__sleeper)
            return sleepers
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_sleeper_by_tax_id(self, tax_id: str) -> Sleeper | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT user_id, name, surname, tax_id, birth_date, gender, created_at FROM sleepers d INNER JOIN users u on u.tax_id = d.sleeper_tax_id WHERE tax_id = '" + tax_id + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._create_sleeper(row)
                return self.__sleeper
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_sleeper(self, sleeper: Sleeper):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "INSERT INTO sleepers (sleeper_tax_id) VALUES ('" + sleeper.get_tax_id() + "')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_sleeper(self, sleeper: Sleeper):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "UPDATE sleepers SET sleeper_tax_id = '" + sleeper.get_tax_id() + "' WHERE sleeper_tax_id = '" + sleeper.get_tax_id() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_sleeper(self, sleeper: Sleeper):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "DELETE FROM sleepers WHERE sleeper_tax_id = '" + sleeper.get_tax_id() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _create_sleeper(self, row: tuple) -> None:
        self.__sleeper = Sleeper()
        self.__sleeper.set_user_id(row[self.__USER_ID])
        self.__sleeper.set_name(row[self.__NAME])
        self.__sleeper.set_surname(row[self.__SURNAME])
        self.__sleeper.set_tax_id(row[self.__TAX_ID])
        self.__sleeper.set_birth_date(row[self.__BIRTHDATE])
        self.__sleeper.set_gender(row[self.__GENDER])
        self.__sleeper.set_created_at(row[self.__CREATE_AT])
