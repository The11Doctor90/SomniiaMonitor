#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.dao.inertial_parameter_dao import InertialParameterDAO
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl

from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.inertial_parameter_composite import InertialParameterComposite
from somniiaMonitor.model.inertial_parameter_data import InertialParameterData


class InertialParameterDAOImpl(InertialParameterDAO):
    __PARAMETER_ID, __TIME, __RMS, __ROLL, __PITCH, __YAW, __ANALYSIS_CODE = 0, 1, 2, 3, 4, 5, 6
    __instance = None
    __inertial_parameter: InertialParameterData | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if InertialParameterDAOImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__inertial_parameter = None
            self.__connection = None
            self.__result_set = None
            InertialParameterDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if InertialParameterDAOImpl.__instance is None:
            InertialParameterDAOImpl()
        return InertialParameterDAOImpl.__instance

    def find_inertial_parameter_by_analysis_code(self, analysis_code: str) -> InertialParameterComposite | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM inertial_params WHERE analysis_code = '" + analysis_code + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        inertial_parameters = InertialParameterComposite()
        try:
            for row in self.__result_set.fetchall():
                self._create_inertial_parameter(row)
                inertial_parameters.add_inertial_data(self.__inertial_parameter)
            return inertial_parameters
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def add_inertial_parameter(self, inertial_parameter: InertialParameterData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = f"INSERT INTO inertial_params (time, rms, roll, pitch, yaw, analysis_code) VALUES ({inertial_parameter.get_time()}, {inertial_parameter.get_root_mean_square()}, {inertial_parameter.get_roll()}, {inertial_parameter.get_pitch()}, {inertial_parameter.get_yaw()}, '{inertial_parameter.get_analysis_code()}')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_inertial_parameter(self, inertial_parameter: InertialParameterData):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "DELETE FROM inertial_params WHERE analysis_code = '" + inertial_parameter.get_analysis_code() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _create_inertial_parameter(self, row: tuple) -> None:
        self.__inertial_parameter = InertialParameterData()
        self.__inertial_parameter.set_inertial_parameter_id(row[self.__PARAMETER_ID])
        self.__inertial_parameter.set_time(row[self.__TIME])
        self.__inertial_parameter.set_root_mean_square(row[self.__RMS])
        self.__inertial_parameter.set_roll(row[self.__ROLL])
        self.__inertial_parameter.set_pitch(row[self.__PITCH])
        self.__inertial_parameter.set_yaw(row[self.__YAW])
        self.__inertial_parameter.set_analysis_code(row[self.__ANALYSIS_CODE])
