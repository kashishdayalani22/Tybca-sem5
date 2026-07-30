class Employee:
    def __init__(self):
        self.emp_no = 36
        print("first constructor")

    def __init__(self):
            self.emp_no = 36
            print("second constructor")

    def __init__(self):
        self.emp_no = 36
        print("third constructor")

    def name(self):
        self.emp_name = "kashish"

    def delete(self):
        del self.emp_name

emp1 = Employee()
emp1.emp_salary = 100000
emp1.name()

print(emp1.__dict__)
print()
print(emp1.__dict__.values())

emp1.delete()
print("Again print all instance variable")
print(emp1.__dict__)

del emp1.emp_salary
print("after deleting from outside the class")
print(emp1.__dict__)





