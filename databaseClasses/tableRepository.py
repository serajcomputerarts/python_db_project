from databaseClasses.table import Table
from databaseClasses.database import Database
from databaseClasses.query import Query

class TableRepository:
    table : Table
    def __init__(self, table:Table):
        self.table = table
        
    def __convertData(self,data):
        list : list[type(self)] = []
        for item in data:
            temp = type(self)()
            for column in temp.table.columns:
                setattr(temp,column.name,item[column.name])
            list.append(temp)
        return list
    
    def getListDictionary(self,where : str = "",order: str = ""):
        database = Database()
        query = Query.listQuery(self.table,where,order)
        result = database.executeQuery(query)
        return result

    def getList(self,where : str = "",order: str = ""):
        return self.__convertData(self.getListDictionary(where,order))
    
    def getPageDictionary(self,where : str = "",order: str = "",skip : int = 0,take : int = 10):
        database = Database()
        query = Query.pageQuery(self.table,where,order,skip,take)
        result = database.executeQuery(query)
        return result
        
    def getPage(self,where : str = "",order: str = "",skip : int = 0,take : int = 10):
        return self.__convertData(self.getPageDictionary(where,order,skip,take))

    def getById(self,id):
        primaryColumn = next(filter(lambda c: c.isPrimaryKey(),self.table.columns))
        list = self.getList(f"'{primaryColumn.name}' = '{id}'")
        if(len(list) > 0):
            return list[0]
        
    def getFirst(self,where : str = "",order: str = ""):
        list = self.getList(where,order)
        if(len(list) > 0):
            return list[0]
        
    def getCount(self,where : str = ""):
        database = Database()
        query = Query.countQuery(self.table,where)
        result = database.executeQuery(query)
        return result[0]["count"]

    def add(self,table : Table):
        database = Database()
        query = Query.insertQuery(table)
        database.executeQuery(query)

    def update(self,table : Table):
        database = Database()
        query = Query.updateQuery(table)
        database.executeQuery(query)
    
    def addOrUpdate(self,table : Table):
        database = Database()
        query = Query.insertUpdateQuery(table)
        database.executeQuery(query)
    
    def addRange(self,list : list[Table]):
        for item in list:
            self.add(item)
    
    def updateRange(self,list : list[Table]):
        for item in list:
            self.update(item)

    def addOrUpdateRange(self,list : list[Table]):
        for item in list:
            self.addOrUpdate(item)

    def delete(self,id):
        database = Database()
        query = Query.deleteQuery(self.table,id)
        database.executeQuery(query)

    def deleteRange(self,list : list[str]):
        for item in list:
            self.delete(item)

    def deleteWithCondition(self,where : str):
        database = Database()
        query = Query.deleteWithConditionQuery(self.table,where)
        database.executeQuery(query)

    def deleteAll(self):
        database = Database()
        query = Query.deleteAllQuery(self.table)
        database.executeQuery(query)

    def rawQuery(self,query):
        database = Database()
        result = database.executeQuery(query)
        return result
