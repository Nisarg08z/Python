# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

        
my_ElectricCar = ElectricCar("Tesla", "Model S", "85KWH")
print(my_ElectricCar.brand)
print(my_ElectricCar.model)
print(my_ElectricCar.battery_size)
print(my_ElectricCar.full_name())