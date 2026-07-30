class BCA:
    def __init__(self, no):
        self.no=no
        print("no of student: ", self.no)

fybca = BCA(10)
sybca = BCA(20)
tybca = BCA(30)
print("Total number os students in bca: ",fybca.no+sybca.no+tybca.no)

