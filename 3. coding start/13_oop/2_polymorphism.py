# Polymorphis (Same function name → different output depending on object)

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

animals = [Cat(),Dog()]
for a in animals:
    a.sound()

#sound() behaves differently depending on object