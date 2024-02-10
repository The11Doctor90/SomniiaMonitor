#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.ekg_parameter_dao import EkgParameterDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl

from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.ekg_parameter_composite import EkgParameterComposite
from somniiaMonitor.model.ekg_parameter_data import EkgParameterData


class EkgParameterDAOImpl(EkgParameterDAO):
    __PARAMETER_ID, __TIME, __HR, __HRV, __RR, __ANALYSIS_ID = 0, 1, 2, 3, 4, 5
    __instance = None
    __ekg_parameter: EkgParameterData | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if EkgParameterDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__ekg_parameter = None
            self.__connection = None
            self.__result_set = None
            EkgParameterDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if EkgParameterDAOImpl.__instance is None:
            EkgParameterDAOImpl()
        return EkgParameterDAOImpl.__instance

    def find_ekg_parameter_by_analysis_id(self, analysis_id: int) -> EkgParameterComposite | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"SELECT * FROM ekg_parameters WHERE fk_analysis_id = {analysis_id}"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        ekg_parameters = EkgParameterComposite()
        try:
            for row in self.__result_set.fetchall():
                self._build_ekg_parameter(row)
                ekg_parameters.add_ekg_data(self.__ekg_parameter)
            return ekg_parameters
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_ekg_parameter(self, ekg_parameter: EkgParameterData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO ekg_parameters (time, hr, hrv, rr_interval, fk_analysis_id) VALUES ({ekg_parameter.get_time()}, {ekg_parameter.get_heart_rate()}, {ekg_parameter.get_heart_rate_variability()}, {ekg_parameter.get_rr_interval()}, {ekg_parameter.get_analysis_id()})"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _build_ekg_parameter(self, row: tuple) -> None:
        self.__ekg_parameter = EkgParameterData()
        self.__ekg_parameter.set_ekg_parameter_id(row[self.__PARAMETER_ID])
        self.__ekg_parameter.set_time(row[self.__TIME])
        self.__ekg_parameter.set_heart_rate(row[self.__HR])
        self.__ekg_parameter.set_heart_rate_variability(row[self.__HRV])
        self.__ekg_parameter.set_rr_interval(row[self.__RR])
        self.__ekg_parameter.set_analysis_id(row[self.__ANALYSIS_ID])
