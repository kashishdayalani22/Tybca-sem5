class FOS:
    class BCA_Dept:
        def total_addmission(self):
            print("No. of admitted students: 240")
            print("Name of department: BCA\n")
    class Chemistry_Dept:
        def total_addmission(self):
            print("No. of admitted students: 160")
            print("Name of department: Chemistry_Dept\n")
    class Maths_Dept:
        def total_addmission(self):
            print("No. of admitted students: 140")
            print("Name of department: Maths_Dept\n")

    def BCA_info(self):
        print("Number of students: 250")
        print("Number of faculties: 5")

    def display(self):
        obj1 = FOS.BCA_Dept()
        obj2 = FOS.Chemistry_Dept()
        obj3 = FOS.Maths_Dept()

        obj1.total_addmission()
        obj2.total_addmission()
        obj3.total_addmission()
a = FOS()
a.display()
a.BCA_info()