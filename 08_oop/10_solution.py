# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        print("This car has a battery.")

class Engine:
    def engine_info(self):
        print("This car has an engine.")

class ElectricCar(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar("Tesala", "Model S")
my_new_tesla.battery_info()
my_new_tesla.engine_info()
        