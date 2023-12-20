from databaseClasses.table import Table
from databaseClasses.column import columnSqlType

class Query:
    def checkTableQuery(table : Table):
        return f"PRAGMA table_info('{table.tableName}')"
    
    def identityQuery(table : Table):
        return f"SELECT * FROM sqlite_master WHERE tbl_name=='{table.tableName}'"
    
    def deleteQuery(table : Table):
        return f"DROP TABLE IF EXISTS {table.tableName}"
    
    def createTableQuery(table : Table):
        query = f"CREATE TABLE IF NOT EXISTS '{table.tableName}' ("
        for column in table.columns:
            query += f"'{column.name}' {columnSqlType(column.dataType).upper()}"
            if(column.isPrimaryKey()):
                query += " PRIMARY KEY"
            if(column.isIncrement()):
                query += " AUTOINCREMENT"
            if(column.nullable == False):
                query += " NOT NULL"
            query += ","
        query = query[:-1]
        query += ")"
        return query
    
    def listQuery(table : Table,where : str = "",order: str = ""):
        query = f"SELECT * FROM [{table.tableName}]"
        if(len(where) > 0):
            query += f" WHERE {where}"
        if(len(order) > 0):
            query += f" ORDER BY {order}"
        return query
    
    def pageQuery(table : Table,where : str = "",order: str = "",skip : int = 0,take : int = 10):
        query = f"SELECT * FROM [{table.tableName}]"
        if(len(where) > 0):
            query += f" WHERE {where}"
        if(len(order) > 0):
            query += f" ORDER BY {order}"
        query += f" LIMIT {skip},{take}"
        return query
    
    def insertQuery(table : Table):
        query = f"INSERT INTO {table.tableName}("
        for column in table.columns:
            if(column.isIncrement() == False):
                query += f"[{column.name}],"
        query = query[:-1]
        query += ") VALUES("
        for column in table.columns:
            if(column.isIncrement() == False):
                query += f"{column.getSqlValue(table)},"
        query = query[:-1]
        query += ")"
        return query
    
    def updateQuery(table : Table):
        query = f"UPDATE [{table.tableName}] SET "
        for column in table.columns:
            if(column.isPrimaryKey() == False):
                query += f"[{column.name}] = {column.getSqlValue(table)},"
        query = query[:-1]
        primaryColumn = next(filter(lambda c: c.isPrimaryKey(),table.columns))
        query += f" WHERE [{primaryColumn.name}] = '{primaryColumn.getSqlValue(table)}'"
        return query
    
    def insertUpdateQuery(table : Table):
        query = f"INSERT OR REPLACE INTO [{table.tableName}]("
        for column in table.columns:
            if(column.isIncrement() == False):
                query += f"[{column.name}],"
        query = query[:-1]
        query += ") VALUES("
        for column in table.columns:
            if(column.isIncrement() == False):
                query += f"{column.getSqlValue(table)},"
        query = query[:-1]
        query += ")"
        return query
    
    def deleteQuery(table : Table,id):
        query = f"DELETE FROM [{table.tableName}]"
        primaryColumn = next(filter(lambda c: c.isPrimaryKey(),table.columns))
        query += f" WHERE [{primaryColumn.name}] = '{id}'"
        return query
    
    def deleteAllQuery(table : Table):
        query = f"DELETE FROM [{table.tableName}]"
        return query
    
    def deleteWithConditionQuery(table : Table,where : str):
        query = f"DELETE FROM [{table.tableName}]"
        query += f" WHERE {where}"
        return query
    
    def countQuery(table : Table,where : str = ""):
        query = f"SELECT COUNT(*) AS count FROM [{table.tableName}]"
        if(len(where) > 0):
            query += f" WHERE {where}"
        return query