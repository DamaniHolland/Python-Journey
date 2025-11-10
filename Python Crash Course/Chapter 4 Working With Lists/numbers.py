###############################################################################
#   Damani Holland
#   11/09/2025
#   CS Python
###############################################################################

# Making Numerical List

'''
Using the Range() Function

The range() function helps to generate a series of numbers
The output stops one short of the value you put for 'y'

Syntax:

    - for variable_name in range(x, y):
            print(variable_name)
'''

for value in range(1,5):
    print(value)
    
'''
Using range() to Make a List of Numbers

By placing the range() function inside of the list() function
the output generates a range of numbers and puts them in a list

Syntax:

    - variable_name = list(range(x,y))
      print(variable_name) 
'''

numbers = list(range(1,6))
print(numbers)