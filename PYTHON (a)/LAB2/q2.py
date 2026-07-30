class abc:
    def get_String(self,str):
        self.empty_string = str

    def print_String(self):
        print(self.empty_string.upper())

a1= abc()
a1.get_String("hello")
a1.print_String()
