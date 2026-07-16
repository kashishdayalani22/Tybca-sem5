class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

    def m1(self):
        del self.d


test1 = Test()
print(test1.__dict__)
test1.m1()
print(test1.__dict__)
del test1.c
print(test1.__dict__)