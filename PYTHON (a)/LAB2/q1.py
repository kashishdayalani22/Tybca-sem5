class Test:
    def average(self, numbers):
        avg = sum(numbers)/len(numbers)
        print("average of list",avg)
        return avg

l = [10 , 20 , 30 , 40 , 50]
a1 = Test()
a1.average(l)
