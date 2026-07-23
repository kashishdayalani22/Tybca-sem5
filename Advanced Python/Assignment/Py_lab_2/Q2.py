class ABC:
    def get_String(self, str):
        self.empty_str = str

    def print_String(self):
        print(self.empty_str.upper())

a1 = ABC()
a1.get_String("hello")
a1.print_String()