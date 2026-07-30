class Employee:
    def __init__(self,name, salary):
        self.Emp_name = name
        self.Emp_salary = salary

class Workingdays:
    def __init__(self):
        self.total_working_days = 24

    def __mul__(self, other):
        print(self.total_working_days*other.Emp_salary)

Emp = Employee("kashish",10000)
Workingday = Workingdays()
Workingday*Emp