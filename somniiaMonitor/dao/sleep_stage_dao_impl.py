#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.sleep_stage_dao import SleepStageDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl

from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.sleep_stage_composite import SleepStageComposite
from somniiaMonitor.model.sleep_stage_data import SleepStageData


class SleepStageDAOImpl(SleepStageDAO):
    __STAGE_ID, __TIME, __STAGE, __ANALYSIS_ID = 0, 1, 2, 3
    __instance = None
    __sleep_stage: SleepStageData | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if SleepStageDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__sleep_stage = None
            self.__connection = None
            self.__result_set = None
            SleepStageDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if SleepStageDAOImpl.__instance is None:
            SleepStageDAOImpl()
        return SleepStageDAOImpl.__instance

    def find_sleep_stage_by_analysis_id(self, analysis_id: int) -> SleepStageComposite | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM sleep_stages WHERE fk_analysis_id = {analysis_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        sleep_stages = SleepStageComposite()
        try:
            for row in self.__result_set.fetchall():
                self._build_sleep_stage(row)
                sleep_stages.add_sleep_stage_data(self.__sleep_stage)
            return sleep_stages
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_sleep_stage(self, sleep_stage: SleepStageData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO sleep_stages (time, stage, fk_analysis_id) VALUES ({sleep_stage.get_time()}, {sleep_stage.get_stage()}, {sleep_stage.get_analysis_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _build_sleep_stage(self, row: tuple) -> None:
        self.__sleep_stage = SleepStageData()
        self.__sleep_stage.set_sleep_stage_id(row[self.__STAGE_ID])
        self.__sleep_stage.set_time(row[self.__TIME])
        self.__sleep_stage.set_stage(row[self.__STAGE])
        self.__sleep_stage.set_analysis_id(row[self.__ANALYSIS_ID])
