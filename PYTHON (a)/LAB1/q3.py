class test:
     def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
     def m1(self):
        del self.d

t1=test()
print(t1.__dict__)
t1.m1()
print(t1.__dict__)

del t1.c
print(t1.__dict__)

