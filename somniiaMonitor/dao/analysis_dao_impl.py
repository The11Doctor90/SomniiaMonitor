#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.dao.analysis_dao import AnalysisDAO
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.analysis import Analysis


class AnalysisDAOImpl(AnalysisDAO):
    __ANALYSIS_ID, __START, __STOP, __CODE, __SLEEPER_ID, __DOCTOR_ID, __MASK_ADDR = 0, 1, 2, 3, 4, 5, 6
    __ROW_ALONE = 0
    __instance = None
    __analysis: Analysis | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if AnalysisDAOImpl.__instance is not None:
            raise RuntimeError("This class is a singleton!")
        else:
            self.__analysis = None
            self.__connection = None
            self.__result_set = None
            AnalysisDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if AnalysisDAOImpl.__instance is None:
            AnalysisDAOImpl()
        return AnalysisDAOImpl.__instance

    def find_all_analyses(self) -> list[Analysis] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM analyses"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        analyses = []
        try:
            for row in self.__result_set.fetchall():
                self._create_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analyses_by_sleeper_tax_id(self, tax_id: str) -> list[Analysis] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM analyses WHERE sleeper_tax_id = '" + tax_id + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        analyses = []
        try:
            for row in self.__result_set.fetchall():
                self._create_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analyses_by_doctor_tax_id(self, tax_id: str) -> list[Analysis] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM analyses WHERE doctor_tax_id = '" + tax_id + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        analyses = []
        try:
            for row in self.__result_set.fetchall():
                self._create_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analyses_by_mask_mac_address(self, mask_mac_address: str) -> list[Analysis] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM analyses WHERE mask_mac_addr = '" + mask_mac_address + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        analyses = []
        try:
            for row in self.__result_set.fetchall():
                self._create_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analyses_by_code(self, analyses_code: str) -> Analysis | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM analyses WHERE code = '" + analyses_code + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._create_analyses(row)
                return self.__analysis
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def add_analyses(self, analysis: Analysis):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "INSERT INTO analyses (start, stop, code, sleeper_tax_id, doctor_tax_id, mask_mac_addr) VALUES ('" + analysis.get_start() + "','" + analysis.get_stop() + "','" + analysis.get_analysis_code() + "','" + analysis.get_sleeper_tax_id() + "', '" + analysis.get_doctor_tax_id() + "', '" + analysis.get_mask_address() + "')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_analyses(self, analyses: Analysis):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "UPDATE analyses SET stop = '" + analyses.get_stop() + "' WHERE code = '" + analyses.get_analysis_code() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_analyses(self, analyses: Analysis):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "DELETE FROM analyses WHERE code = '" + analyses.get_analysis_code() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count


    def _create_analyses(self, row: tuple) -> None:
        self.__analysis = Analysis()
        self.__analysis.set_analysis_id(row[self.__ANALYSIS_ID])
        self.__analysis.set_start(row[self.__START])
        self.__analysis.set_stop(row[self.__STOP])
        self.__analysis.set_analysis_code(row[self.__CODE])
        self.__analysis.set_sleeper_tax_id(row[self.__SLEEPER_ID])
        self.__analysis.set_doctor_tax_id(row[self.__DOCTOR_ID])
        self.__analysis.set_mask_address(row[self.__MASK_ADDR])
