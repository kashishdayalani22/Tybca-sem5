class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("the area of circle is:" , 3.14*self.radius**2)

    def circumference(self ):
        print("the circumference of circle is",2*3.14*self.radius)

obj1=circle(5)
obj1.area()
obj1.circumference()