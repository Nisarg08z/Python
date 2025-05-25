# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fule_type(self):
        return "Gasoline"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fule_type(self):
        return "Electric"
    
safari = Car("Tata", "safari")
print(safari.fule_type())

tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(tesla.fule_type())