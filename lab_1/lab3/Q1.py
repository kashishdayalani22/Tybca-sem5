class Employee:
    Emp_name = "ANUBHAV"
    emp_department = "BCA"
    emp_salary = -50500

    def display(self):
        print(Employee.Emp_name)
        print(Employee.emp_department)
        print(Employee.emp_salary)
    
class UpdateEmp(Employee):
    def updateinfo(self, salary, emp_department):
        Employee.emp_salary = salary
        Employee.emp_department = emp_department

Emp1 = Employee()
Emp2 = UpdateEmp()
Emp1.display()
Emp2.updateinfo(-150000, "TYBCA")
Emp1.display()