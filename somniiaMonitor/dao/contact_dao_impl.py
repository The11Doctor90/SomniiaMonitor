#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.contact_dao import ContactDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.contact import Contact


class ContactDAOImpl(ContactDAO):
    __CONTACT_ID, __EMAIL, __PHONE, __ADDRESS, __NUMBER = 0, 1, 2, 3, 4
    __CITY, __PROVINCE, __ZIP_CODE, __COUNTRY, __USER_ID = 5, 6, 7, 8, 9
    __ROW_ALONE = 0
    __instance = None
    __contact: Contact | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if ContactDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__contact = None
            self.__connection = None
            self.__result_set = None
            ContactDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if ContactDAOImpl.__instance is None:
            ContactDAOImpl()
        return ContactDAOImpl.__instance

    def find_all_contacts(self) -> list[Contact] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM contacts"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        contacts = []
        try:
            for row in self.__result_set.fetchall():
                self._build_contact(row)
                contacts.append(self.__contact)
            return contacts
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_contact_by_user_id(self, user_id: int) -> Contact | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM contacts WHERE fk_user_id = {user_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_contact(row)
                return self.__contact
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_contact_by_email(self, email: str) -> Contact | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM contacts WHERE email = '{email}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_contact(row)
                return self.__contact
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_contact_by_phone(self, phone: str) -> Contact | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM contacts WHERE phone = '{phone}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_contact(row)
                return self.__contact
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_contact(self, contact: Contact):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO contacts (email, phone, address, number, city, province, zip, country, fk_user_id) VALUES ('{contact.get_email()}','{contact.get_phone()}','{contact.get_address()}','{contact.get_number()}', '{contact.get_city()}', '{contact.get_province()}', '{contact.get_zip_code()}', '{contact.get_country()}', {contact.get_user_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_contact(self, contact: Contact):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"UPDATE contacts SET email = '{contact.get_email()}', phone = '{contact.get_phone()}', address = '{contact.get_address()}', number = '{contact.get_number()}', city = '{contact.get_city()}', province = '{contact.get_province()}', zip = '{contact.get_zip_code()}', country = '{contact.get_country()}', tax_id = {contact.get_user_id()} WHERE fk_user_id = {contact.get_user_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_contact(self, contact: Contact):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"DELETE FROM contacts WHERE fk_user_id = {contact.get_user_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def contact_exist(self, user_id: str):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM contacts WHERE fk_user_id = {user_id}"
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

    def _build_contact(self, row: tuple) -> None:
        self.__contact = Contact()
        self.__contact.set_contact_id(row[self.__CONTACT_ID])
        self.__contact.set_email(row[self.__EMAIL])
        self.__contact.set_phone(row[self.__PHONE])
        self.__contact.set_address(row[self.__ADDRESS])
        self.__contact.set_number(row[self.__NUMBER])
        self.__contact.set_city(row[self.__CITY])
        self.__contact.set_province(row[self.__PROVINCE])
        self.__contact.set_zip_code(row[self.__ZIP_CODE])
        self.__contact.set_country(row[self.__COUNTRY])
        self.__contact.set_user_id(row[self.__USER_ID])
