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
    __ANALYSIS_ID, __START, __STOP, __SLEEPER_ID, __CODE, __DOCTOR_ID, __MASK_ID = 0, 1, 2, 3, 4, 5, 6
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
                self._build_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analyses_by_sleeper_id(self, sleeper_id: int) -> list[Analysis] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM analyses WHERE fk_sleeper_id = {sleeper_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        analyses = []
        try:
            for row in self.__result_set.fetchall():
                self._build_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analyses_by_doctor_id(self, doctor_id: str) -> list[Analysis] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM analyses WHERE fk_doctor_id = {doctor_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        analyses = []
        try:
            for row in self.__result_set.fetchall():
                self._build_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analyses_by_mask_id(self, mask_id: str) -> list[Analysis] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM analyses WHERE fk_mask_id= {mask_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        analyses = []
        try:
            for row in self.__result_set.fetchall():
                self._build_analyses(row)
                analyses.append(self.__analysis)
            return analyses
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_analysis_by_id(self, analyses_id: str) -> Analysis | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM analyses WHERE analysis_id = {analyses_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_analyses(row)
                return self.__analysis
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def find_analysis_by_code(self, analyses_code: str) -> Analysis | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM analyses WHERE code = '{analyses_code}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._build_analyses(row)
                return self.__analysis
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def add_analysis(self, analysis: Analysis):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO analyses (code, fk_sleeper_id, fk_doctor_id, fk_mask_id) VALUES ('{analysis.get_code()}', {analysis.get_sleeper_id()}, {analysis.get_doctor_id()}, {analysis.get_mask_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_analysis(self, analyses: Analysis):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"UPDATE analyses SET stop = '{analyses.get_stop()}' WHERE analysis_id = {analyses.get_analysis_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_analysis(self, analyses: Analysis):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"DELETE FROM analyses WHERE analysis_id = {analyses.get_analysis_id()}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _build_analyses(self, row: tuple) -> None:
        self.__analysis = Analysis()
        self.__analysis.set_analysis_id(row[self.__ANALYSIS_ID])
        self.__analysis.set_start(row[self.__START])
        self.__analysis.set_stop(row[self.__STOP])
        self.__analysis.set_code(row[self.__CODE])
        self.__analysis.set_sleeper_id(row[self.__SLEEPER_ID])
        self.__analysis.set_doctor_id(row[self.__DOCTOR_ID])
        self.__analysis.set_mask_id(row[self.__MASK_ID])
