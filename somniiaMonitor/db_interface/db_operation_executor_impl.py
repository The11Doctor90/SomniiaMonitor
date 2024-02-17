#  Copyright (c) Matteo Ferreri 2024.
"""
public class DbOperationExecutor {
    private final List<IDbOperation> dbOperations = new ArrayList<>();

    public ResultSet executeReadOperation(IDbOperation<ResultSet> dbOp){
        this.dbOperations.add(dbOp);
        return dbOp.execute();
    }

    public int executeWriteOperation(IDbOperation<Integer> dbOp){
        this.dbOperations.add(dbOp);
        return dbOp.execute();
    }

}
"""
from sqlite3 import Cursor

from somniiaMonitor.db_interface.db_operation import DbOperation


class DbOperationExecutorImpl:
    __DB_OPERATION: list[DbOperation] = []

    def execute_read_operation(self, db_operation: DbOperation) -> Cursor:
        self.__DB_OPERATION.append(db_operation)
        return db_operation.execute_operation()

    def execute_write_operation(self, db_operation: DbOperation) -> int:
        self.__DB_OPERATION.append(db_operation)
        return db_operation.execute_operation()