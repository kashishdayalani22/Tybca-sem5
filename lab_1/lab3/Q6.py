class Test:
    count = 0
    def __init__(self):
        print("initailizing constructor")
        Test.count+=1

    def __del__(self):
        print("deleteing Activity")

t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
print("refernece variable: ",Test.count)

t1 = None
t2 = None
t3 = None
t4 = None


