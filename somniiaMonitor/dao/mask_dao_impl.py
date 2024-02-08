#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq
from sqlite3 import Cursor

from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.dao.mask_dao import MaskDAO
from somniiaMonitor.db_interface.db_connection_impl import DbConnectionImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl
from somniiaMonitor.db_interface.db_update_operation_impl import DbUpdateOperationImpl
from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.model.mask import Mask


class MaskDAOImpl(MaskDAO):
    __MASK_ID, __MAC_ADDR, __NAME, __STATUS = 0, 1, 2, 3
    __ROW_ALONE = 0
    __instance = None
    __mask: Mask | None
    __connection: DbConnection | None
    __result_set: Cursor | None

    def __init__(self):
        if MaskDAOImpl.__instance is not None:
            raise RuntimeError("This class is a singleton!")
        else:
            self.__mask = None
            self.__connection = None
            self.__result_set = None
            MaskDAOImpl.__instance = self

    @staticmethod
    def get_instance():
        if MaskDAOImpl.__instance is None:
            MaskDAOImpl()
        return MaskDAOImpl.__instance

    def find_all_masks(self) -> list[Mask] | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM masks"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)

        masks = []
        try:
            for row in self.__result_set.fetchall():
                self._create_mask(row)
                masks.append(self.__mask)
            return masks
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()
        return None

    def find_mask_by_mac_address(self, mac_addr: str) -> Mask | None:
        self.__connection = DbConnectionImpl.get_instance()
        sql = "SELECT * FROM masks WHERE mac_addr = '" + mac_addr + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbReadOperationImpl(sql)
        self.__result_set = db_operation_executor.execute_read_operation(db_operation)
        rows = self.__result_set.fetchall()
        try:
            if len(rows) == 1:
                row = rows[self.__ROW_ALONE]
                self._create_mask(row)
                return self.__mask
        except sq.Error as e:
            print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
        except Exception as e:
            print(f"ResultSet: {e.args}")
        finally:
            self.__connection.close_connection()

        return None

    def add_mask(self, mask: Mask):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "INSERT INTO masks (mac_addr, name, status) VALUES ('" + mask.get_mac_addr() + "','" + mask.get_name() + "','" + mask.get_status() + "')"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def update_mask(self, mask: Mask):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "UPDATE masks SET mac_addr = '" + mask.get_mac_addr() + "', name = '" + mask.get_name() + "', status = '" + mask.get_status() + "' WHERE mac_addr = '" + mask.get_mac_addr() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def delete_mask(self, mask: Mask):
        self.__connection = DbConnectionImpl.get_instance()
        sql = "DELETE FROM masks WHERE mac_addr = '" + mask.get_mac_addr() + "'"
        db_operation_executor = DbOperationExecutorImpl()
        db_operation = DbUpdateOperationImpl(sql)
        row_count = db_operation_executor.execute_write_operation(db_operation)
        self.__connection.close_connection()
        return row_count

    def _create_mask(self, row: tuple) -> None:
        self.__mask = Mask()
        self.__mask.set_mask_id(row[self.__MASK_ID])
        self.__mask.set_mac_addr(row[self.__MAC_ADDR])
        self.__mask.set_name(row[self.__NAME])