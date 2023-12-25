from services.studentService import StudentService
from tables.student import Student

studentService = StudentService()
# s.deleteAll()
# s.addRandomStudents()
# stu = Student()
# stu.sname = "ali"
# stu.scity = "tehran"
# stu.sadd = "P124"
# studentService.add(stu)
list = studentService.getList()
print(list[0].sname)
dictList = studentService.getListDictionary()
print(dictList)
count = studentService.getCount()
print(count)