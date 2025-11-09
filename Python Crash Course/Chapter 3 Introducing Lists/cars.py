###############################################################################
#   Damani Holland
#   11/08/2025
#   CS Python
###############################################################################

# Organizing A List

'''
Sorting a List Permanently With The sort() Method
Organizes the list alphabetically permanently

Syntax
    - list_name.sort()
'''

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

'''
You can reverse the order of alphbetical sorting using the attribute 'reverse=True'
This also permanently changes the list

Syntax
    - list_name.sort(reverse=True)
'''

cars.sort(reverse=True)
print("Reversed Order:", cars)
cars.sort()

'''
You can change the order of the list without changing original list using sorted() function
putting the list in alphabetical order

Syntax
    - sorted(list_name)
    
You can add the reverse attribute to the sorted() function using 'reverse=True'

Syntax
    - sorted(list_name, reverse=True)
'''

cars = ["bmw", "audi", "toyota", "subaru"]
print("This is the original order:", cars)
print("This is the changed list:", sorted(cars, reverse=True))
print("This is the original list again:", cars)

'''
Printing a list in reverse order using the reverse() method

Syntax
    - list_name.reverse()
'''
# Original list of cars
print(cars)

# Reverse the order of original list (non-alphbetically) permanently
cars.reverse()

# New list of cars
print(cars)

# revert back to original order by applying .reverse() again
cars.reverse()

'''
Finding the Length of a list using len() method

Syntax
    - len(list_name)
'''
# Prints original list of cars
print(cars)
# prints the number of items in list
print(len(cars))
