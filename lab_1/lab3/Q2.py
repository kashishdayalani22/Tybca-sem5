class Person:
    Name = "Anubhav"
    def display(self):
        print(Person.Name)
        Dis = Person.DOB()
        Dis.display()
    class DOB:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yyyy = 1947
        def display(self):
            print(f"DOB: {self.dd}/{self.mm}/{self.yyyy}")

P1 = Person()

P1.display()