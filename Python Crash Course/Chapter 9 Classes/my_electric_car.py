###############################################################################
#   Damani Holland
#   7/6/2026
#   CS Python
###############################################################################

# Inheritance
'''
If the class you're writing is a specialized version of another class you wrote, 
 you can use inheritance. When one class inherits from another, it automatically 
 takes on all attributes and methods of the first class.
 '''
    

class Car():
    
    """A simple attempt to represent a car."""
    
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
    """A simple Attempt to model a battery for an electric car."""
    
    def __init__(self,battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery")            

    def get_range(self):
        """Print a statemnet about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range == 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        # Initilize attributes of the parent class.
        super(ElectricCar, self).__init__(make, model, year)
        
        # Initialize attributes specific to an electric car.
        self.battery_size = 70
        self.battery = Battery()
        
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
            
car_One = Car('toyota','avalon', 2002)

my_Tesla = ElectricCar('tesla', 'model s', 2016)
print(my_Tesla.get_descriptive_name())



my_Tesla.battery.describe_battery()
my_Tesla.battery.get_range( ) 