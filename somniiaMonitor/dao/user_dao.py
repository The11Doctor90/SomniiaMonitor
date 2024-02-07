#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.db_interface.db_operation_executor import DbOperationExecutor
from somniiaMonitor.dao.interface_user_dao import IUserDAO
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.db_interface.db_read_operation import DbReadOperation
from somniiaMonitor.db_interface.db_update_operation import DbUpdateOperation
from somniiaMonitor.db_interface.interface_db_connection import IDbConnection
from somniiaMonitor.model.user import User

class UserDAO(IUserDAO):
    __NAME, __SURNAME, __TAX_ID, __BIRTHDATE, __GENDER, __CREATE_AT = 0, 1, 2, 3, 4, 5
    __instance = None
    __user: User | None
    __connection: IDbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if UserDAO.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__user = None
            self.__connection = None
            self.__result_set = None
            UserDAO.__instance = self

    @staticmethod
    def get_instance():
        if UserDAO.__instance is None:
            UserDAO()
        return UserDAO.__instance

    def find_all_users(self) -> list[User] | None:
        self.__connection = DbConnection().get_instance()
        sql = "SELECT * FROM users"
        db_operation_executor = DbOperationExecutor()
        db_operation = DbReadOperation(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        users = []
        try:
            for user in self.__result_set.fetchall():
                users.append(user)
            return users
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def find_user_by_tax_id(self, tax_id: int) -> User | None:
        self.__connection = DbConnection().get_instance()
        sql = "SELECT * FROM users WHERE tax_id = tax_id"
        db_operation_executor = DbOperationExecutor()
        db_operation = DbReadOperation(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

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
        self.__connection = DbConnection().get_instance()
        sql = "INSERT INTO users (name, surname, tax_id, birth_date, gender) VALUES ('" + user.get_name() + "','" + user.get_surname() + "','" + user.get_tax_id() + "','" + user.birth_date() + "', '" + user.get_gender() + "')"
        db_operation_executor = DbOperationExecutor()
        db_operation = DbUpdateOperation(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_user(self, user: User):
        pass

    def delete_user(self, user: User):
        pass


"""

"""

