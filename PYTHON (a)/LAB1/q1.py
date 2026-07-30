class student:
    def __init__(self):
        self.name= "kashish"
        self.no = 36
        self.marks = 50

    def talk(self):
        print("hello my Name is :" ,self.name)
        print("hello my rollno is :", self.no)
        print("hello my marks are :", self.marks)

s1=student()
s2=student()
s3=student()

s1.talk()

print(id(s1.name))
print(id(s2.name))
print(id(s3.name))