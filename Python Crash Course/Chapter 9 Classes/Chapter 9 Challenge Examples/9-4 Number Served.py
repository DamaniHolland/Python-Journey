###############################################################################
#   Damani Holland
#   7/5/2026
#   CS Python
###############################################################################

'''

9-1. Restaurant: Make a class called Restaurant . The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type . 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open .Make an instance called restaurant from your class . Print the two attri-
butes individually, and then call both methods.

'''
'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . 
Add an attribute called number_served with a default value of 0 . Create an 
instance called restaurant from this class . Print the number of customers the 
restaurant has served, and then change this value and print it again .Add a method called set_number_served() that lets you set the number 
of customers that have been served . Call this method with a new number and 
print the value again .Add a method called increment_number_served() that lets you increment 
the number of customers who’ve been served . Call this method with any num-
ber you like that could represent how many customers were served in, say, a 
day of business.

'''

    
    
    
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("\nResturant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        print("\n--Congradulations!--")
        print(self.restaurant_name + " is now open and serving " + self.cuisine_type + " food.")
        
    def set_number_served(self, customers_served):
        if customers_served >= self.number_served:
            self.number_served = customers_served
        else:
            print("You can't unserve customers.")
        
    def increment_number_served(self, total_customers):
        self.number_served += total_customers
        print(self.restaurant_name + " has now served " + str(self.number_served))
        
restaurant_One = Restaurant("pepe's pizzaria", "Italian")

restaurant_One.open_restaurant()

restaurant_One.describe_restaurant()

print("This restaurant has served " + str(restaurant_One.number_served) + " people")

restaurant_One.set_number_served(10)

restaurant_One.increment_number_served(500)
restaurant_One.set_number_served(499)
