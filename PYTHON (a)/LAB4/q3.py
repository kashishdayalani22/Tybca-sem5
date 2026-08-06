class Department:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print("Department class method...")


class MSU:
    def __init__(self):
        self.department = Department()

    def m2(self):
        print("Msu has a department...")
        print(self.department.a)
        print(self.department.b)
        self.department.m1()


m = MSU()
m.m2()
