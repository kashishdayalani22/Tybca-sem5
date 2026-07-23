class abc:
    obj_count = 0
    def __init__(self):
        abc.obj_count += 1

    @staticmethod
    def no_of_obj():
        print("no of objects: ", abc.obj_count)

obj1 = abc()
obj2 = abc()
obj3 = abc()
obj4 = abc()
obj5 = abc()
obj6 = abc()

abc.no_of_obj()
