class AxisBank:
    def __init__(self):
        self.balance = 0
        self.print_options()

    def print_options(self):
        print("Select your Option: ")
        print("1. Deposite")
        print("2. Withdraw")
        print("3. Display")
        print("4. Exit \n")
        x = int(input("enter your choice"))
        self.operation(x)

    def Deposite(self, amt):
        self.balance += amt
        print("deposite done \n")

    def Withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            print("withdraw done\n ")
        else:
            print("insufficient \n")

    def Display(self):
        print("current balance: ", self.balance)

    def operation(self, choice):
        if choice == 1:
            amt = int(input("enter the amount: "))
            self.Deposite(amt)
            self.print_options()
        elif choice == 2:
            amt = int(input("enter the amount: "))
            self.Withdraw(amt)
            self.print_options()
        elif choice == 3:
            self.Display()
            self.print_options()
        elif choice == 4:
            print("Exit!!")

obj = AxisBank()