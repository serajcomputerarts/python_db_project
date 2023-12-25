from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Student(Table):
    sid : Column('sid',ColumnDataType.idIncrement) = 0
    sname : Column('sname',ColumnDataType.string) = ''
    scity : Column('scity', ColumnDataType.string) = ''
    sadd : Column('sadd', ColumnDataType.string) = ''

    def __init__(self):
        super().__init__()
    
