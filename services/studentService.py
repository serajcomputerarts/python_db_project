from databaseClasses.tableRepository import TableRepository
from tables.student import Student
import random
import string


class StudentService(TableRepository):
    def  __init__(self):
        super().__init__(Student())

    def addRandomStudents(self,count:int = 10):
        names=["hadi","reza","ali","kazem"]
        city=["tabriz","Tehran","shiraz"]
        add=["P11","p300","P40","p60"]
        for i in range(count):
            stu = Student()
            stu.sname = random.choice(names)
            stu.scity = random.choice(city)
            stu.sadd = random.choice(add)
            self.add(stu)