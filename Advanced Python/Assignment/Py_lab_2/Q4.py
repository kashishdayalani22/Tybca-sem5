class InvoiceItem:
    def __init__(self, ID, description, quantity, unit_price):
        self.id = ID
        self.desc = description
        self.quntity = quantity
        self.price = unit_price

    def getTotal(self):
        self.Total = self.quntity * self.price
        print("Total invoice: ", self.Total)

obj = InvoiceItem(110758, "a very strange item", 4, 550)
obj.getTotal()
