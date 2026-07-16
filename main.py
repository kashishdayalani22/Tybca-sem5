class student:
    def __init__(self, name, marks, rollno):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print(f"Hello My Name is: {self.name} \n My Rollno is: {self.rollno} \n My Marks are: {self.marks}")


std1 = student("Gunjan", 20, 40)
std2 = student("Anubhav", 50, 8)
std3 = student("Kashish", 37, 31)

print(id(std1.name))
print(id(std2.name))
print(id(std3.name))