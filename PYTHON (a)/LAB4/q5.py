class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color;

    def getinfo(self):
        print("Car Information:")
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")


class Employee:
    def __init__(self, emp_name, emp_no, car):
        self.emp_name = emp_name
        self.emp_no = emp_no
        self.car = car

    def empinfo(self):
        print("Employee Information:")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Number: {self.emp_no}")
        self.car.getinfo()

car_obj = Car("Toyota", "Corolla", "Blue")
emp_obj = Employee("John Doe", 101, car_obj)

emp_obj.empinfo()