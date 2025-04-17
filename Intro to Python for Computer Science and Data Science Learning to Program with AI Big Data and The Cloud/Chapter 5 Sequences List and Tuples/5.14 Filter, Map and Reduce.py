###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# Filtering a Sequence's Values with the Built-in filter Function

numbers= [ 10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def is_odd(x):
    """Returns True only if x is odd."""
    return x % 2 != 0

print(list(filter(is_odd, numbers)))

'''
same result as code above
'''

print([item for item in numbers if is_odd(item)])

# Using a Lambda Rather than a Function

'''
Use lambda to define the function inline where it's needed
'lambda parameter_list: expression'
'''

print(list(filter(lambda x: x % 2 != 0, numbers)))

# Mapping a Sequence's Values to New Values

print(numbers)

print(list(map(lambda x: x ** 2, numbers)))

'''
same result as code above
'''

print([item ** 2 for item in numbers])

# Combining filter and map

'''
First 'filter()' returns only odd values, Second ' map()' returns an iterable
of squares from filtered values. finally list uses map's iterable to create the
list
'''
print(list(map(lambda x: x ** 2,
            filter(lambda x: x % 2 != 0, numbers))))

'''
Uses list's comprehension to create same results as above
'''

print([x ** 2 for x in numbers if x % 2 != 0])

# 5.14 Exercise 3

'''
Create a list called numbers containing 1 through 15, then perform
the following tasks:
a) Use the built-in function filter with a lambda to select only numbers’ even elements.
Create a new list containing the result.
b) Use the built-in function map with a lambda to square the values of numbers’ elements.
Create a new list containing the result.
c) Filter numbers’ even elements, then map them to their squares. Create a new list
containing the result.
'''

numbers = list(range(1, 16))
print(numbers)

new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(new_numbers)

new_map_numbers = list(map(lambda x: x ** 2, numbers))
print(new_map_numbers)

square_of_evens = list(map(lambda x: x ** 2,
                           filter(lambda x: x % 2 == 0, numbers)))

print(square_of_evens)

# 5.14 Exercise 4

'''
Map a list of the three Fahrenheit temperatures 41, 32 and 212 to
a list of tuples containing the Fahrenheit temperatures and their Celsius equivalents. Convert
Fahrenheit temperatures to Celsius with the following formula:
Celsius = (Fahrenheit – 32) * (5 / 9)
'''

temp = list(map(lambda x: ((x, (x - 32) * 5 / 9)), [41, 32, 212]))
print(temp)