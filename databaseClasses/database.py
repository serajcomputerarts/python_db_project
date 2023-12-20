import sqlite3
from databaseClasses.table import Table
from databaseClasses.column import columnSqlType
from databaseClasses.query import Query
from tables.student import Student
from tables.book import Book
from tables.sale import Sale

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Database :
    __con : sqlite3.Connection = None
    tables : list[Table] = [
        Student(),
        Book(),
        Sale()
    ]
    DataBaseName = "mylib.db"
    __cur : sqlite3.Cursor = None


    
    def __init__(self):
        if(Database.__con == None):
            Database.__con = sqlite3.connect(self.DataBaseName)
            Database.__cur = Database.__con.cursor()
            Database.__onOpen(self)
            Database.__con.row_factory = dict_factory

    def __onOpen(self):
        for table in self.tables:
            delete = self.__checkTable(table)
            if(delete == True) :
               query = Query.deleteQuery(table)
               self.executeQuery(query)

            query = Query.createTableQuery(table)
            self.executeQuery(query)

    def __checkTable(self,table : Table = None):
        query = Query.checkTableQuery(table)
        res = self.executeQuery(query)
        if(len(res) != len(table.columns)):
            return True
        else:
            for item in res:
                name = item["name"]
                column = next(filter(lambda c: c.name == c.name == name,table.columns))
                if(column == None):
                    return True
                else:
                    nullable = item["notnull"] == 0 and item["pk"] == 0
                    if(column.nullable != nullable):
                        return True
                    primary = item["pk"] == 1
                    if(column.isPrimaryKey() != primary):
                        return True
                    columnType = columnSqlType(column.dataType)
                    type = item["type"]
                    if (columnType.lower() != type.lower()):
                        return True
                    if(column.isPrimaryKey()):
                        query = Query.identityQuery(table)
                        res = self.executeQuery(query)
                        if ((res[0]["sql"].upper().find("AUTOINCREMENT") != -1) != column.isIncrement()):
                            return True
        return False
    def executeQuery(self,query : str = ""):
        Database.__cur.execute(query)
        Database.__con.commit()
        res = [dict_factory(Database.__cur, row) for row in Database.__cur.fetchall()]
        return res
    

