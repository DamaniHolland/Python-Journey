###############################################################################
#   Damani Holland
#   7/8/2026
#   CS Python
###############################################################################

# Storing Multiple Classes

"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range == 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        
        self.battery_size = 70
        self.battery = Battery()
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        
    def fill_gas_tank():
        print("This car doesn't have a gas tank!")
    