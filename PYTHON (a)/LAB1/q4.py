class test:
        def __init__(self):
                self.a=10
                self.b=20
                self.c=30
                self.d=40

t1=test()
t2=test()

del t1.a

print("all instance variable from t1")
print(t1.__dict__)

print("all instance variable from t2")
print(t2.__dict__)