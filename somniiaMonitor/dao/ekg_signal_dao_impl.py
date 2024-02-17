#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.ekg_signal_dao import EkgSignalDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl

from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.ekg_signal_composite import EkgSignalComposite
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgSignalDAOImpl(EkgSignalDAO):
    __SIGNAL_ID, __TIME, __SIGNAL, __ANALYSIS_ID = 0, 1, 2, 3
    __instance = None
    __ekg_signal: EkgSignalData | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if EkgSignalDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__ekg_signal = None
            self.__connection = None
            self.__result_set = None
            EkgSignalDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if EkgSignalDAOImpl.__instance is None:
            EkgSignalDAOImpl()
        return EkgSignalDAOImpl.__instance

    def find_ekg_signal_by_analysis_id(self, analysis_id: int) -> EkgSignalComposite | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM ekg_signals WHERE analysis_id = '{analysis_id}'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        ekg_signals = EkgSignalComposite()
        try:
            for row in self.__result_set.fetchall():
                self._build_ekg_signal(row)
                ekg_signals.add_ekg_data(self.__ekg_signal)
            return ekg_signals
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_ekg_signal(self, ekg_signal: EkgSignalData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO ekg_signals (time, ekg_signal, fk_analysis_id) VALUES ({ekg_signal.get_time()}, {ekg_signal.get_signal()}, {ekg_signal.get_analysis_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _build_ekg_signal(self, row: tuple) -> None:
        self.__ekg_signal = EkgSignalData()
        self.__ekg_signal.set_ekg_signal_id(row[self.__SIGNAL_ID])
        self.__ekg_signal.set_time(row[self.__TIME])
        self.__ekg_signal.set_signal(row[self.__SIGNAL])
        self.__ekg_signal.set_analysis_id(row[self.__ANALYSIS_ID])
