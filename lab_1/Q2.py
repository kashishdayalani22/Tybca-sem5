class Person:
    name = "ABC"

    def display(self):
        print("person name is: ", self.name)
        obj = Person.DOB()
        obj.display()

    class DOB:
        mm = 5
        dd = 10
        yyyy = 1947
        def display(self):
            print("person age is: ", self.dd, "/", self.mm, "/", self.yyyy)

p1 = Person()
p1.display()