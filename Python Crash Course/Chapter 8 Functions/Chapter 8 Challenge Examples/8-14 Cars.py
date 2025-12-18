###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################

'''

8-14. Cars: Write a function that stores information about a car in a diction-
ary . The function should always receive a manufacturer and a model name . It 
should then accept an arbitrary number of keyword arguments . Call the func-
tion with the required information and two other name-value pairs, such as a 
color or an optional feature . Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was 
stored correctly.

'''

def make_car(manufacturer, model, **car_info):
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    
    for key, value in car_info.items():
        car_profile[key] = value
        
    return car_profile

car = make_car('toyota', 'avalon', color='green', tow_package=True)
print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)