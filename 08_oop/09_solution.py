# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
                    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
                        
my_tesla = ElectricCar('Tesla', 'Model S', 2019)
print(isinstance(my_tesla, Car))  # Output: True
print(isinstance(my_tesla, ElectricCar))  # Output: True
                        