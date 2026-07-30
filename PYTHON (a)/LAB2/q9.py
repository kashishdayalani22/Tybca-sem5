class Student:
    def __init__(self, name, rollNo, total_marks):
        self.name = name
        self.rollno = rollNo
        self.marks = total_marks
    def display(self):
        print("Name : ", self.name)
        print("Roll Number : ", self.rollno)
        print("Marks : ", self.marks)

    def grade(self):
        if self.marks >= 90:
            print("Grade: A")

        elif self.marks >= 70:
            print("Grade: B")

        elif self.marks >= 50:
            print("Grade: C")

        else:
            print("Grade : F")

s1 = Student("abc", 10, 90)
s1.display()
s1.grade()