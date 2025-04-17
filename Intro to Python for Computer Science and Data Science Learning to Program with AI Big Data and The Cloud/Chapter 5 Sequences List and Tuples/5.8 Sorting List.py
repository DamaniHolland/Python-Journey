###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# 5.8 Sorting Lists

'''
Sorting a List in Ascending Order
List method '.sort()' modifies a list to arrange its elements in ascending order
'''

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

print('Random order: ', numbers)

numbers.sort() # '.sort()' sorts values in list in ascending order

print('Ascending order: ', numbers)

'''
Sorting a List in Descending Order
Call list method '.sort()' with the optional keyword argument 'reverse' set to 
True
'''

numbers.sort(reverse = True)

print('Descending order: ', numbers)

'''
Built-In Function 'sorted()'
Sorted returns a new list containing sorted elements
The original sequence is unmodified
'''

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

ascending_numbers = sorted(numbers)
print('Old list: ', numbers)
print('Sorted Ascending New list: ', ascending_numbers) # notice we assigned a new variable to new list

letters = 'fasgchjebi'

ascending_letters = sorted(letters) # it works alphabetically as well

print('Original List: ', letters)
print('Sorted List: ', ascending_letters)

colors = ('red', 'orange', 'yellow', 'green', 'blue')

ascending_colors = sorted(colors)

print('Old List: ', colors)
print('Sorterd List: ', ascending_colors)

# 5.8 Exercise 3

'''
Create a foods list containing 'Cookies', 'pizza', 'Grapes',
'apples', 'steak' and 'Bacon'. Use list method sort to sort the list in ascending order.
Are the strings in alphabetical order?
'''

foods_list = ['Cookies', 'pizza', 'grapes', 'apples', 'steak', 'Bacon']

foods_list.sort()

print(foods_list) # The capital letters take priority when sorting.
# the list is not in alphabetical order