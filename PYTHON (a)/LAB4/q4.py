class Engine:
    a = "Static Variable of Engine"
    def __init__(self, b):
        self.b = b

    def m1(self):
        print("This is Engine class method….")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def m2(self):
        print("Accessing Engine class from Car class:")
        print("Static variable a:", Engine.a)
        print("Instance variable b:", self.engine.b)
        self.engine.m1()

engine_obj = Engine(50)
car_obj = Car(engine_obj)
car_obj.m2()