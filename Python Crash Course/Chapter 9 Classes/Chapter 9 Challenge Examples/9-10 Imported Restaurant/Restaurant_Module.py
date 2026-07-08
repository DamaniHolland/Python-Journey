###############################################################################
#   Damani Holland
#   7/8/2026
#   CS Python
###############################################################################
"""

9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
ule . Make a separate file that imports Restaurant . Make a Restaurant instance, 
and call one of Restaurant’s methods to show that the import statement is work-
ing properly

"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        name = self.restaurant_name
        cuisine_type = self.cuisine_type
        
        message = "Restaurant Information:"
        message += "\n\tReastaurant name: " + name.title()
        message += "\n\tCuisine type: " + cuisine_type.title()
        
        print(message)
        
    def open_restaurant(self):
        message = "Grand Opening!"
        message += "\n\tWelcome to: " + self.restaurant_name.title()
        
        print(message)
        
        