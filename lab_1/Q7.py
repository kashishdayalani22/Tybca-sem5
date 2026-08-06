class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatanddrink(self):
        print("Eat biryani and Drink coca cola")


class Employee(Person):
    def __init__(self, name, age, emp_no, emp_salary):
        super().__init__(name, age)
        self.emp_no = emp_no
        self.emp_salary = emp_salary

    def empinfo(self):
        print("Employee Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee Number: {self.emp_no}")
        print(f"Employee Salary: {self.emp_salary}")

person_obj = Person("Rahul", 30)
person_obj.eatanddrink()

print()
emp_obj = Employee("Anita", 28, 101, 50000)
emp_obj.empinfo()
emp_obj.eatanddrink()
