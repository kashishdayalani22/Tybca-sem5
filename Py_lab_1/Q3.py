class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.d

a1 = Test()
print(a1.__dict__)
a1.m1()
print(a1.__dict__)
del a1.c
