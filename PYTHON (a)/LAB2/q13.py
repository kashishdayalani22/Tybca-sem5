class Person:
    name = "kapil"

    def display(self):
        print(Person.name)
        obj = Person.DOB()
        obj.display()

    class DOB:
        mm = 5
        dd = 10
        yyyy = 1947

        def display(self):
            print(f"DOB : {self.dd}/{self.mm}/{self.yyyy}")


p1 = Person()
p1.display()