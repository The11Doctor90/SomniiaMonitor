#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.dao.sleeper_dao import SleeperDAO
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.sleeper import Sleeper


class SleeperDAOImpl(SleeperDAO):
    __SLEEPER_ID, __NAME, __SURNAME, __TAX_ID, __BIRTHDATE = 0, 1, 2, 3, 4
    __GENDER, __CREATE_AT, __USER_ID, __CONTACT_ID = 5, 6, 7, 8
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
        sql = f"SELECT sleeper_id, name, surname, tax_id, birth_date, gender, created_at, fk_user_id, fk_contact_id FROM sleepers s INNER JOIN users u on s.fk_user_id = u.user_id"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        sleepers = []
        try:
            for row in self.__result_set.fetchall():
                self._build_sleeper(row)
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
        sql = f"SELECT sleeper_id, name, surname, tax_id, birth_date, gender, created_at, fk_user_id, fk_contact_id FROM sleepers s INNER JOIN users u on s.fk_user_id = u.user_id WHERE u.tax_id = '{tax_id}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_sleeper(row)
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
        sql = f"INSERT INTO sleepers (fk_user_id) VALUES ('{sleeper.get_user_id()}')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_sleeper(self, sleeper: Sleeper):
        pass

    def delete_sleeper(self, sleeper: Sleeper):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"DELETE FROM sleepers WHERE sleeper_id = {sleeper.get_sleeper_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def sleeper_exist_by_tax_id(self, tax_id: str) -> bool:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM sleepers WHERE tax_id = '{tax_id}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                return True
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return False

    def sleeper_exist_by_id(self, sleeper_id: int) -> bool:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM sleepers WHERE sleeper_id = '{sleeper_id}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                return True
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return False

    def _build_sleeper(self, row: tuple) -> None:
        self.__sleeper = Sleeper()
        self.__sleeper.set_sleeper_id(row[self.__SLEEPER_ID])
        self.__sleeper.set_name(row[self.__NAME])
        self.__sleeper.set_surname(row[self.__SURNAME])
        self.__sleeper.set_tax_id(row[self.__TAX_ID])
        self.__sleeper.set_birth_date(row[self.__BIRTHDATE])
        self.__sleeper.set_gender(row[self.__GENDER])
        self.__sleeper.set_created_at(row[self.__CREATE_AT])
        self.__sleeper.set_user_id(row[self.__USER_ID])
        self.__sleeper.set_contact_id(row[self.__CONTACT_ID])
