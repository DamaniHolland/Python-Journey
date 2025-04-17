###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# Passing an Entire List to a Function

def modify_elements(items):
    """Multiplies all elements i items by 2."""
    for i in range(len(items)):
        items[i] *= 2 # takes each element in items and multiples it by 2 and replaces original value
        
numbers = [10, 3, 7, 1, 9]

modify_elements(numbers)
print(numbers)

'''
Passing a Tuple to a Function
Since tuple's are immutable(unable to modify), trying to pass the tuple into
the modify_element function creates a TypeError
'''
numbers_tuple = (10, 20, 30)

print(numbers_tuple)

# Remove (#) to see
 
#modify_elements(numbers_tuple)

# print(numbers_tuple)