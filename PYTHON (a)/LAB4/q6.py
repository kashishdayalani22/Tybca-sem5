class Parent:
    def m1(self):
        print("Parent class method...")


class Child(Parent):
    def m2(self):
        print("Child class method...")


p = Parent()
p.m1()
c = Child()
c.m1()
c.m2()