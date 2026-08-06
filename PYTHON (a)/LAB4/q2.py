class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student(8.30)
s2 = Student(9.18)
print(s1 > s2)