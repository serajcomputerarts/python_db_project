from databaseClasses.table import  Table
from databaseClasses.column import  Column ,ColumnDataType

class  Book(Table):
    bid : Column('bid',ColumnDataType.idIncrement) = 0
    btitle : Column('btitle',ColumnDataType.string) = ''
    bauther : Column('bauther', ColumnDataType.string) = ''
    bprice : Column('bprice', ColumnDataType.int) = ''

    def __init__(self):
        super().__init__()
    
