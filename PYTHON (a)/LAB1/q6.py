class student:
    clg_name="MSU"

    def __init__(selfself):
        student.class_name = "S3"

    def abc(selfself):
        student.faculty_name = "DCA"

s1=student()
s1.abc()



student.teacher_name="kashish"
print(student.__dict__)
print()
print(student.__dict__.values())

del student.clg_name
del student.class_name
del student.faculty_name
del student.teacher_name

print(student.__dict__)