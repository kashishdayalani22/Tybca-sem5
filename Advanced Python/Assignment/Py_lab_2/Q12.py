class A:
    def m1(self):
        print("this is instance method")

    @staticmethod
    def m2():
        print("this is static method")

    @classmethod
    def m3(cls):
        print("this is class method")


a = A()
a.m1()
a.m2()
a.m3()