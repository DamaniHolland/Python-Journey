###############################################################################
#   Damani Holland
#   7/7/2026
#   CS Python
###############################################################################

'''
9-9. Battery Upgrade: Use the final version of electric_car.py from this section . 
Add a method to the Battery class called upgrade_battery() . This method 
should check the battery size and set the capacity to 85 if it isn’t already . 
Make an electric car with a default battery size, call get_range() once, and 
then call get_range() a second time after upgrading the battery . You should 
see an increase in the car’s range.
'''

class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer += miles

class Battery():
    
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("\nThis car has a " + str(self.battery_size) + " -kwh battery.")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270   

        message = "\nThis car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            message = "\nCongradulations!"
            message += "\nYou have upgraded your battery to an "
            message += str(self.battery_size) + "-kwh battery."
            print(message)
        
        else:
            message = "\nThe car's battery has already been upgraded to an "
            message += str(self.battery_size) + "-kwh battery."
            print(message)
            
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        
        self.battery_size = 70
        self.battery = Battery()
        
    def describe_battery(self):
        print("\nThis car has a " + str(self.battery_size) + "-kwh battery.")
        
    def fill_gas_tank():
        print("\nThis car doesn't have a gas tank!")
        
car_One = Car('toyota', 'avalon', 2002)

my_Tesla = ElectricCar('tesla', 'model s', 2016)
print(my_Tesla.get_descriptive_name())

my_Tesla.battery.describe_battery()
my_Tesla.battery.get_range()
my_Tesla.battery.upgrade_battery()
my_Tesla.battery.upgrade_battery()
my_Tesla.battery.get_range()