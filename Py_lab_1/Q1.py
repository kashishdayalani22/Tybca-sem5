class Student:
    """part a and b"""

    def __init__(self):
        self.name = "Gunjan"
        self.no = 40
        self.marks = 8

    '''part c and d'''

    def talk(self):
        print("Hello My name is ", self.name)
        print("My roll no. is ", self.no)
        print("My Marks ", self.marks)
        print()


'''part e'''
s1 = Student()
s2 = Student()
s3 = Student()

s1.talk()
'''part f'''
print(id(s1.name))
print(id(s2.name))
print(id(s3.name))
