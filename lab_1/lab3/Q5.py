import time

class Test:
    def __init__(self):
        print("Object Initialization...")
    def __del__(self):
        print("Performing clean up activities...")
t1 = Test()
t1 = None
time.sleep(50)
print("End of Application….")
