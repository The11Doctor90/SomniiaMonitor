#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.eeg_signal_dao import EegSignalDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.eeg_signal_composite import EegSignalComposite
from somniiaMonitor.model.eeg_signal_data import EegSignalData


class EegSignalDAOImpl(EegSignalDAO):
    __SIGNAL_ID, __TIME, __CHANNEL_1, __CHANNEL_2, __CHANNEL_3, __ANALYSIS_ID = 0, 1, 2, 3, 4, 5
    __instance = None
    __eeg_signal: EegSignalData | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if EegSignalDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__eeg_signal = None
            self.__connection = None
            self.__result_set = None
            EegSignalDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if EegSignalDAOImpl.__instance is None:
            EegSignalDAOImpl()
        return EegSignalDAOImpl.__instance

    def find_eeg_signal_by_analysis_id(self, analysis_id: int) -> EegSignalComposite | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM eeg_signals WHERE eeg_signals.fk_analysis_id = {analysis_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        eeg_signals = EegSignalComposite()
        try:
            for row in self.__result_set.fetchall():
                self._build_eeg_signal(row)
                eeg_signals.add_eeg_data(self.__eeg_signal)
            return eeg_signals
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def add_eeg_signal(self, eeg_signal: EegSignalData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO eeg_signals (time, channel_1, channel_2, channel_3, fk_analysis_id) VALUES ({eeg_signal.get_time()}, {eeg_signal.get_first_channel()}, {eeg_signal.get_second_channel()}, {eeg_signal.get_third_channel()}, {eeg_signal.get_analysis_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _build_eeg_signal(self, row: tuple) -> None:
        self.__eeg_signal = EegSignalData()
        self.__eeg_signal.set_eeg_signal_id(row[self.__SIGNAL_ID])
        self.__eeg_signal.set_time(row[self.__TIME])
        self.__eeg_signal.set_first_channel(row[self.__CHANNEL_1])
        self.__eeg_signal.set_second_channel(row[self.__CHANNEL_2])
        self.__eeg_signal.set_third_channel(row[self.__CHANNEL_3])
        self.__eeg_signal.set_analysis_id(row[self.__ANALYSIS_ID])
