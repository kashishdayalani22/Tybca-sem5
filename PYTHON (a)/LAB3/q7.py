class Test:
    def __init__(self):
        print("initailizing constructor")

    def __del__(self):
        print("Deleting references")

list1 = [Test(), Test(), Test(), Test()]
list1=None