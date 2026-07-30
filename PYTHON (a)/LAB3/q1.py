class Employee:
    def __init__(self, name, department, salary):
        self.emp_name = name
        self.emp_department = department
        self.emp_salary = salary

    def display(self):
        print("Name:", self.emp_name)
        print("Department:", self.emp_department)
        print("Salary:", self.emp_salary)

class UpdateEmp:
    def updateinfo(self, emp, new_department, new_salary):
        emp.emp_department = new_department
        emp.emp_salary = new_salary

e1 = Employee("Kashish", "HR", 50000)
print("Before Update:")
e1.display()
updater = UpdateEmp()
updater.updateinfo(e1, "IT", 100000)
print("\nAfter Update:")
e1.display()