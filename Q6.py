class Student:
    clg_name = "msu"
    class_name = "TYBCA"
    faculty_name = "DCA"
    teacher_name = "Gunjan"


st1 = Student()
print(Student.__dict__)
print(Student.clg_name)
print(Student.class_name)
print(Student.faculty_name)
print(Student.teacher_name)

del Student.clg_name
del Student.class_name
del Student.faculty_name
del Student.teacher_name
print(Student.__dict__)