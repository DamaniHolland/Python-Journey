###############################################################################
#   Damani Holland
#   12/28/2025
#   CS Python
###############################################################################



# Working with Classes and Instances

    # The car class
class car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = car ('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

    # Setting a Default Value for an Attribute
    
class Car():
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

    # Modifying Attribute Values
"""Change value of odometer_reading using 'assign' to change it directly"""
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

    # Modifying an Attribute's Value Through a Method
    
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = (str(self.year) + ' ' + self.make + ' ' + self.model)
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, milage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")
            
    # Incrementing an Attribute's Value Through A Method
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_used_car.update_odometer(2)
my_used_car.read_odometer()