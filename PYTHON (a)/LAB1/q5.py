class test:
        def __init__(self):
                self.a=10
                self.b=20

t1=test()
t2=test()



t1.a=100000

print(t1.__dict__)
print(t2.__dict__)