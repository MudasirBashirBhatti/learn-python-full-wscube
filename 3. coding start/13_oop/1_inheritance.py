# Inheritance (One class uses another class’s features.)

class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal): # Dog class inherits from Animal class
    def speak(self): 
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
