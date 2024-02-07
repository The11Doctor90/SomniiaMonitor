#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.utils_dao import *
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.dao.user_dao import UserDAO
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.user import User

class UserDAOImpl(UserDAO):
    __NAME, __SURNAME, __TAX_ID, __BIRTHDATE, __GENDER, __CREATE_AT = 0, 1, 2, 3, 4, 5
    __instance = None
    __user: User | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if UserDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__user = None
            self.__connection = None
            self.__result_set = None
            UserDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if UserDAOImpl.__instance is None:
            UserDAOImpl()
        return UserDAOImpl.__instance

    def find_all_users(self) -> list[User] | None:
        self.__connection = DbConnectionImpl().get_instance()
        sql = "SELECT * FROM users"
        self.__result_set = get_read_operation_execution(sql)

        if self.__connection is not None:
            return get_all_entities(self.__connection, self.__result_set)

        return None

    def find_user_by_tax_id(self, tax_id: str) -> User | None:
        self.__connection = DbConnectionImpl().get_instance()
        sql = "SELECT * FROM users WHERE tax_id = '" + tax_id + "'"
        self.__result_set = get_read_operation_execution(sql)

        try:
            if self.__result_set.rowcount == 1:
                row = self.__result_set.fetchone()
                self.__user = User()
                self.__user.set_name(row[self.__NAME])
                self.__user.set_surname(row[self.__SURNAME])
                self.__user.set_tax_id(row[self.__TAX_ID])
                self.__user.set_birth_date(row[self.__BIRTHDATE])
                self.__user.set_gender(row[self.__GENDER])
                self.__user.set_created_at(row[self.__CREATE_AT])
                return self.__user
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def add_user(self, user: User):
        self.__connection = DbConnectionImpl().get_instance()
        sql = "INSERT INTO users (name, surname, tax_id, birth_date, gender) VALUES ('" + user.get_name() + "','" + user.get_surname() + "','" + user.get_tax_id() + "','" + user.birth_date() + "', '" + user.get_gender() + "')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_user(self, user: User):
        self.__connection = DbConnectionImpl().get_instance()
        sql = "UPDATE users SET name = '" + user.get_name() + "', surname = '" + user.get_surname() + "', tax_id = '" + user.get_tax_id() + "', birth_date = " + user.birth_date() + ", gender = '" + user.get_gender() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_user(self, user: User):
        self.__connection = DbConnectionImpl().get_instance()
        sql = "DELETE FROM users WHERE tax_id = '" + user.get_tax_id() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

