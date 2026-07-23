class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of circle: ", 3.14 * self.radius ** 2)

    def circumference(self):
        print("Circumference of circle: ", 2 * 3.14 * self.radius)

obj1 = circle(4)
obj1.area()
obj1.circumference()