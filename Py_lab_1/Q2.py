class Employee:
    def __init__(self):
        print("first constructor")
        self.emp_no = 101

    def __init__(self):
        print("second constructor")
        self.emp_no = 101

    def __init__(self):
        print("third constructor")
        self.emp_no = 101

    def name(self):
        self.emp_name = "Anubhav Singh"

    def delete(self):
        del self.emp_name

emp1 = Employee()
emp1.emp_salary = 50000
emp1.name()

print(emp1.__dict__)
print()
print(emp1.__dict__.values())
print()
emp1.delete()
print("after calling delete")
print(emp1.__dict__)
print()
del emp1.emp_salary
print("after deleting from ousode the class")
print(emp1.__dict__)