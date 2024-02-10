#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.ppg_parameter_dao import PpgParameterDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl

from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.ppg_parameter_composite import PpgParameterComposite
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData


class PpgParameterDAOImpl(PpgParameterDAO):
    __PARAMETER_ID, __TIME, __HR, __SPO2, __PI, __BR, __ANALYSIS_ID = 0, 1, 2, 3, 4, 5, 6
    __instance = None
    __ppg_parameter: PpgParameterData | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if PpgParameterDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__ppg_parameter = None
            self.__connection = None
            self.__result_set = None
            PpgParameterDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if PpgParameterDAOImpl.__instance is None:
            PpgParameterDAOImpl()
        return PpgParameterDAOImpl.__instance

    def find_ppg_parameter_by_analysis_id(self, analysis_id: int) -> PpgParameterComposite | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM ppg_params WHERE fk_analysis_id = {analysis_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        ppg_parameters = PpgParameterComposite()
        try:
            for row in self.__result_set.fetchall():
                self._build_ppg_parameter(row)
                ppg_parameters.add_ppg_data(self.__ppg_parameter)
            return ppg_parameters
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_ppg_parameter(self, ppg_parameter: PpgParameterData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO ppg_params (time, hr, spo2, pi, br, fk_analysis_id) VALUES ({ppg_parameter.get_time()}, {ppg_parameter.get_heart_rate()}, {ppg_parameter.get_spo2()}, {ppg_parameter.get_perfusion_index()}, {ppg_parameter.get_breath_frequency()}, {ppg_parameter.get_analysis_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _build_ppg_parameter(self, row: tuple) -> None:
        self.__ppg_parameter = PpgParameterData()
        self.__ppg_parameter.set_ppg_parameter_id(row[self.__PARAMETER_ID])
        self.__ppg_parameter.set_time(row[self.__TIME])
        self.__ppg_parameter.set_heart_rate(row[self.__HR])
        self.__ppg_parameter.set_spo2(row[self.__SPO2])
        self.__ppg_parameter.set_perfusion_index(row[self.__PI])
        self.__ppg_parameter.set_breath_frequency(row[self.__BR])
        self.__ppg_parameter.set_analysis_id(row[self.__ANALYSIS_ID])
