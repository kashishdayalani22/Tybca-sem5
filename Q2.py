class Employee():
    def __init__(self, name):
        print("1st constructor")

    def __init__(self, name, emp_name):
        print("1st constructor")

    def __init__(self):
        self.emp_no = 12

    def Emp_details(self):
        self.emp_name = "Gunjan"

    def delete(self):
        del self.emp_name

emp = Employee()
emp.Emp_details()
emp.emp_salary = 10000
print(emp.emp_no)
print(emp.emp_name)
print(emp.emp_salary)
print(emp.__dict__)
del emp.emp_salary
emp.delete()
# print(emp.emp_name)
# print(emp.emp_salary)
# print(emp.__dict__)