from services.studentService import StudentService
from tables.student import Student

s = StudentService()
# s.deleteAll()
# s.addRandomStudents()
list = s.getList()
print(list[0].sname)
a = s.getListDictionary()
print(a)