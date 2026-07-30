class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, o):
        return self.a + o.a


ob1 = A(10)
ob2 = A(20)
ob3 = A("Dhyey")
ob4 = A("Patel")
print(ob1 + ob2)
print(ob3 + ob4)
