#  Copyright (c) Matteo Ferreri 2024.
import sqlite3 as sq

from somniiaMonitor.db_interface.db_connection import DbConnection
from somniiaMonitor.db_interface.db_operation_executor_impl import DbOperationExecutorImpl
from somniiaMonitor.db_interface.db_read_operation_impl import DbReadOperationImpl


def get_read_operation_execution(sql: str):
    db_operation_executor = DbOperationExecutorImpl()
    db_operation = DbReadOperationImpl(sql)
    return db_operation_executor.execute_read_operation(db_operation)


def get_all_entities(connection: DbConnection, result_set: sq.Cursor) -> list | None:
    entities = []
    try:
        for entity in result_set.fetchall():
            entities.append(entity)
        return entities
    except sq.Error as e:
        print(f"Si è verificato il seguente errore: {e.sqlite_errorcode}: {e.sqlite_errorname}")
    except Exception as e:
        print(f"ResultSet: {e.args}")
    finally:
        connection.close_connection()
    return None
