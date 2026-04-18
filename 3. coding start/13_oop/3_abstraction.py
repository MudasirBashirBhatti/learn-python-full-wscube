# Abstraction (Hide implementation, show only required structure)

class Car:
    def start(self):
        print("Car started...")

# User sirf start() use karega, andar kya logic hai usko nahi dekhna.

car1 = Car().start()