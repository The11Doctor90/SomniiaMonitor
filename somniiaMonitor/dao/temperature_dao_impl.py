#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.temperature_dao import TemperatureDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl

from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.temperature_composite import TemperatureComposite
from somniiaMonitor.model.temperature_data import TemperatureData


class TemperatureDAOImpl(TemperatureDAO):
    __TEMPERATURE_ID, __TIME, __TEMPERATURE, __ANALYSIS_CODE = 0, 1, 2, 3
    __instance = None
    __temperature: TemperatureData | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if TemperatureDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__temperature = None
            self.__connection = None
            self.__result_set = None
            TemperatureDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if TemperatureDAOImpl.__instance is None:
            TemperatureDAOImpl()
        return TemperatureDAOImpl.__instance

    def find_temperature_by_analysis_code(self, analysis_code: str) -> TemperatureComposite | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM temperatures WHERE analysis_code = '" + analysis_code + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        temperatures = TemperatureComposite()
        try:
            for row in self.__result_set.fetchall():
                self._create_temperature(row)
                temperatures.add_temperature_data(self.__temperature)
            return temperatures
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_temperature(self, temperature: TemperatureData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO temperatures (time, value, analysis_code) VALUES ({temperature.get_time()}, {temperature.get_temperature()}, '{temperature.get_analysis_code()}')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_temperature(self, temperature: TemperatureData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "DELETE FROM temperatures WHERE analysis_code = '" + temperature.get_analysis_code() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _create_temperature(self, row: tuple) -> None:
        self.__temperature = TemperatureData()
        self.__temperature.set_temperature_id(row[self.__TEMPERATURE_ID])
        self.__temperature.set_time(row[self.__TIME])
        self.__temperature.set_temperature(row[self.__TEMPERATURE])
        self.__temperature.set_analysis_code(row[self.__ANALYSIS_CODE])
