class Mathoperation:
    @staticmethod
    def sum(a, b):
        print("a + b = ", a+b)

    @staticmethod
    def product(a, b):
        print("a * b = ", a*b)

    @staticmethod
    def average(a, b):
        print("average of num1 and num2 = ", (a+b)/2)


Mathoperation.sum(15, 20)
Mathoperation.product(15, 20)
Mathoperation.average(15, 20)