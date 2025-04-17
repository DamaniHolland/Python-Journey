###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# del Statement

'''
the del statement can also be used to remove elements from a list and to delete
variables from the interactive session. you can remove from any valid index or 
valid slice
'''

'''
Deleting the elements at a Specific List Index
'''

numbers = list(range(0, 10))

print(numbers)

del numbers[-1] # Uses 'del' to remove the last element

print(numbers)

'''
Deleting a Slice from a List
'''

del numbers[0:2] # Removes the first two elements
print(numbers)

del numbers[::2] # Removes every other element left in the list
print(numbers)

'''
Deleting a Slice Representing the entire List
'''
del numbers[:]
print(numbers)

'''
Deleting a Variable from the Current Session
'''
del numbers # 'del' statement can delete any variable
# remove (#) to see NameError
# print(numbers)

# 5.6 Exercise 2

'''
Create a list called numbers containing the values from 1 through
15, then use the del statement to perform the following operations consecutively:
a) Delete a slice containing the first four elements, then show the resulting list.
b) Starting with the first element, use a slice to delete every other element of the list,
then show the resulting list
'''

numbers = list(range(1, 16))

del numbers[:4]
print(numbers)

del numbers[::2]
print(numbers)