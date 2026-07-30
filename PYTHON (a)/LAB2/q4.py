class invoiceitem:
    def __init__(self,ID,description,quantity,unit_price):
        self.id =ID
        self.desc=description
        self.quantity=quantity
        self.unit=unit_price

    def get_total(self):
        self.total=self.quantity*self.unit
        print("total amount",self.total)

obj1=invoiceitem(11111,"something something",100,100)
obj1.get_total()