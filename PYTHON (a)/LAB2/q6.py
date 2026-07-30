class Dog:
    legs = 4
    def walk(self, animal):
        print(animal, "walks with ", Dog.legs, "legs.....")

obj = Dog()
obj.walk("dog")
obj.walk("cat")
obj.walk("cow")