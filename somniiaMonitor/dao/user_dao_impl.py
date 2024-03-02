#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.dao.user_dao import UserDAO
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.user import User


class UserDAOImpl(UserDAO):
    __USER_ID, __NAME, __SURNAME, __TAX_ID, __BIRTHDATE, __GENDER, __CREATE_AT = 0, 1, 2, 3, 4, 5, 6
    __PASSWORD , __DOCTOR_ID, __SLEEPER_ID, __CONTACT_ID = 7, 8, 9, 10
    __ROW_ALONE = 0
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
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM users"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        users = []
        try:
            for row in self.__result_set.fetchall():
                self._build_user(row)
                users.append(self.__user)
            return users
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_user_by_tax_id(self, tax_id: str) -> User | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM users WHERE tax_id = '" + tax_id + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_user(row)
                return self.__user
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def add_user(self, user: User):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO users (name, surname, tax_id, birth_date, gender, password) VALUES ('{user.get_name()}', '{user.get_surname()}', '{user.get_tax_id()}','{user.get_birth_date()}', '{user.get_gender()}', '{user.get_password()}')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_user(self, user: User):
        self.__connection = DbConnectionImpl.get_instance()
        fk_doctor_id, fk_sleeper_id, fk_contact_id = "", "", ""
        if user.get_doctor_id() is not None:
            fk_doctor_id = f", fk_doctor_id = {user.get_doctor_id()}"
        if user.get_sleeper_id() is not None:
            fk_sleeper_id = f", fk_sleeper_id = {user.get_sleeper_id()}"
        if user.get_contact_id() is not None:
            fk_contact_id = f", fk_contact_id = {user.get_contact_id()}"

        sql = f"UPDATE users SET name = '{user.get_name()}', surname = '{user.get_surname()}', tax_id = '{user.get_tax_id()}', birth_date = '{user.get_birth_date()}', gender = '{user.get_gender()}' {fk_doctor_id} {fk_sleeper_id} {fk_contact_id} WHERE user_id = {user.get_user_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_user(self, user: User):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"DELETE FROM users WHERE user_id = {user.get_user_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)

        self.__connection.close_connection()
        return row_count

    def user_exist(self, tax_id) -> bool:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM users WHERE tax_id = '{tax_id}'"
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

    def check_password(self, email, password):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM users u INNER JOIN contacts c ON u.user_id = c.fk_user_id WHERE c.email = {email} AND u.password = {password}"
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

    def _build_user(self, row: tuple) -> None:
        self.__user = User()
        self.__user.set_user_id(row[self.__USER_ID])
        self.__user.set_name(row[self.__NAME])
        self.__user.set_surname(row[self.__SURNAME])
        self.__user.set_tax_id(row[self.__TAX_ID])
        self.__user.set_birth_date(row[self.__BIRTHDATE])
        self.__user.set_gender(row[self.__GENDER])
        self.__user.set_created_at(row[self.__CREATE_AT])
        self.__user.set_doctor_id(row[self.__DOCTOR_ID])
        self.__user.set_sleeper_id(row[self.__SLEEPER_ID])
        self.__user.set_contact_id(row[self.__CONTACT_ID])
