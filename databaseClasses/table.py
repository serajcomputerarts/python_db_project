from databaseClasses.column import Column

class Table:
    tableName : str()
    columns : list[Column]
    def __init__(self,tableName : str = ""):
        self.tableName = tableName if len(tableName ) > 0  else type(self).__name__
        self.__getColumns()

    def __getColumns(self):
        self.columns = list()
        for c in type(self).__annotations__.keys():
            temp = Column(vars(type(self).__annotations__[c])['name'],vars(type(self).__annotations__[c])['dataType'],vars(type(self).__annotations__[c])['nullable']) 
            self.columns.append(temp)
