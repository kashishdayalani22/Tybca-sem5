class Student:
    clg_name = "MSU"

    def __init__(self):
        Student.class_name = "S3"

    def abc(self):
        Student.faculty_name = "DCA"

s1 = Student()
s1.abc()
Student.teacher_name = "Kashish Dayalani"
print(Student.__dict__)
print(Student.__dict__.values())

del Student.clg_name
del Student.class_name
del Student.teacher_name
del Student.faculty_name

print(Student.__dict__)
