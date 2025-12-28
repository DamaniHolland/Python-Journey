###############################################################################
#   Damani Holland
#   12/20/2025
#   CS Python
###############################################################################

'''

9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three 
different instances from the class, and call describe_restaurant() for each 
instance.

'''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        print("Restaurant name: " + self.name.title())
        print("Cuisine type: " + self.cuisine.title())
        

restaurant_1 = Restaurant('yoko ono', 'japanese')
restaurant_2 = Restaurant('islands', 'american cuisine')
restaurant_3 = Restaurant('jinya ramen express', 'japanese')


restaurant_1.describe_restaurant() 
