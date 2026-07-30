class BCA:
    def __init__(self, no):
        self.no=no
        print("no of student: ", self.no)

fybca = BCA(100)
sybca = BCA(140)
tybca = BCA(120)
print("Total number os students in bca: ",fybca.no+sybca.no+tybca.no)
