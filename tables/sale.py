from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Sale(Table):
    id : Column('id',ColumnDataType.idIncrement) = 0
    bid : Column('bid',ColumnDataType.int) = ''
    sid : Column('sid', ColumnDataType.int) = ''
    bdate : Column('bdate', ColumnDataType.string) = ''

    def __init__(self):
        super().__init__()
    