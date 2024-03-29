#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.doctor_dao import DoctorDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.doctor import Doctor


class DoctorDAOImpl(DoctorDAO):
    __DOCTOR_ID, __NAME, __SURNAME, __TAX_ID, __BIRTHDATE = 0, 1, 2, 3, 4
    __GENDER, __CREATE_AT, __REGISTER_CODE, __SUPERVISOR, __USER_ID, __CONTACT_ID = 5, 6, 7, 8, 9, 10
    __ROW_ALONE = 0
    __instance = None
    __doctor: Doctor | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if DoctorDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__doctor = None
            self.__connection = None
            self.__result_set = None
            DoctorDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if DoctorDAOImpl.__instance is None:
            DoctorDAOImpl()
        return DoctorDAOImpl.__instance

    def find_all_doctor(self) -> list[Doctor] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT doctor_id, name, surname, tax_id, birth_date, gender, created_at, register_code, id_supervisor,  fk_user_id, fk_contact_id FROM doctors d INNER JOIN users u on d.fk_user_id = u.user_id"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        doctors = []
        try:
            for row in self.__result_set.fetchall():
                self._build_doctor(row)
                doctors.append(self.__doctor)
            return doctors
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_doctor_by_tax_id(self, tax_id: str) -> Doctor | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT doctor_id, name, surname, tax_id, birth_date, gender, created_at, register_code, id_supervisor, fk_user_id, fk_contact_id FROM doctors d INNER JOIN users u on d.fk_user_id = u.user_id WHERE u.tax_id = '{tax_id}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_doctor(row)
                return self.__doctor
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_all_doctor_by_supervisor_id(self, supervisor_id: int) -> list[Doctor] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT doctor_id, name, surname, tax_id, birth_date, gender, created_at, register_code, id_supervisor, fk_user_id, fk_contact_id FROM doctors d INNER JOIN users u on d.doctor_id = u.user_id WHERE id_supervisor = '{supervisor_id}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        doctors = []
        try:
            for row in self.__result_set.fetchall():
                self._build_doctor(row)
                doctors.append(self.__doctor)
            return doctors
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_doctor(self, doctor: Doctor):
        self.__connection = DbConnectionImpl.get_instance()
        supervisor_id = ""
        if doctor.get_supervisor_id() is not None:
            supervisor_id = ", supervisor_id"

        sql = f"INSERT INTO doctors (register_code, fk_user_id {supervisor_id}) VALUES ('{doctor.get_register_code()}', {doctor.get_user_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_doctor(self, doctor: Doctor):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"UPDATE doctors SET register_code = '{doctor.get_register_code()}', id_supervisor = '{doctor.get_supervisor_id()}' WHERE doctor_id = {doctor.get_doctor_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_doctor(self, doctor: Doctor):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"DELETE FROM doctors WHERE doctor_id = {doctor.get_tax_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def doctor_exist_by_tax_id(self, tax_id: str) -> bool:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM doctors WHERE tax_id = '{tax_id}'"
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

    def doctor_exist_by_id(self, doctor_id: int) -> bool:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM doctors WHERE sleeper_id = '{doctor_id}'"
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

    def _build_doctor(self, row: tuple) -> None:
        self.__doctor = Doctor()
        self.__doctor.set_doctor_id(row[self.__DOCTOR_ID])
        self.__doctor.set_name(row[self.__NAME])
        self.__doctor.set_surname(row[self.__SURNAME])
        self.__doctor.set_tax_id(row[self.__TAX_ID])
        self.__doctor.set_birth_date(row[self.__BIRTHDATE])
        self.__doctor.set_gender(row[self.__GENDER])
        self.__doctor.set_created_at(row[self.__CREATE_AT])
        self.__doctor.set_register_code(row[self.__REGISTER_CODE])
        self.__doctor.set_supervisor_id(row[self.__SUPERVISOR])
        self.__doctor.set_user_id(row[self.__USER_ID])
        self.__doctor.set_contact_id(row[self.__CONTACT_ID])
