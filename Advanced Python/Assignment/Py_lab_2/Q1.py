class Test:
    def average(self, lists):
        avg = sum(lists)/len(lists)
        print("Average of list is: ", avg)
        return avg

l = [10, 20, 30, 40, 50]
a1 = Test()
a1.average(l)