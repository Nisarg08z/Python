# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.



class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "This is a car."
    
    
my_car = Car("Tata", "safari")
print(Car.general_description())
