###############################################################################
#   Damani Holland
#   7/6/2026
#   CS Python
###############################################################################

"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of 
the class will work; just pick the one you like better . Add an attribute called 
flavors that stores a list of ice cream flavors . Write a method that displays 
these flavors . Create an instance of IceCreamStand, and call this method.
"""

'''

9-1. Restaurant: Make a class called Restaurant . The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type . 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open .Make an instance called restaurant from your class . Print the two attri-
butes individually, and then call both methods

'''

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        name = self.restaurant_name
        cuisine_type = self.cuisine_type
        message = "Restaurant Information:"
        message += "\n\tRestaurant name: " + name.title()
        message += "\n\tCuisine type: " + cuisine_type.title()
        print(message)
        
    def open_restaurant(self):
        message = "Grand Opening!" 
        message += "\nWelcome to" + " " + self.restaurant_name.title()
        print(message)
        

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocoalate', 'strawberry']

    def describe_flavors(self):
        print(self.flavors)

restaurant_One = Restaurant("pepe's pizzaria" , "italian")
stand_One = IceCreamStand("pepe's freezeria", "soft serve icecream")

print(restaurant_One.restaurant_name)
print(restaurant_One.cuisine_type)
restaurant_One.describe_restaurant()
restaurant_One.open_restaurant()

stand_One.describe_flavors()