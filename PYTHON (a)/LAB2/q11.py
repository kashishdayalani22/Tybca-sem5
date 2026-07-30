class Person:
    @staticmethod
    def isAdult(age):
        if age >= 18:
            print("a legal Adult")
        else:
            print("not an Adult")

p1 = Person()
p1.isAdult(16)