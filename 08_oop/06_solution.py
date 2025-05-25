# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created


class Car:
    
    total_car = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
Car("Tata", "safari")
Car("Tata2", "safari2")
Car("Tata3", "safari3")
Car("Tata4", "safari4")

print(Car.total_car)