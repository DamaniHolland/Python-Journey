###############################################################################
#   Damani Holland
#   11/09/2025
#   CS Python
###############################################################################

squares = []
for value in range(1,11):
    squares.append(value**2)
    
print(squares)

'''
list Comprehensions

This concept allows you to generate a list of numbers in just one line of code.

Syntax:

    - variable_name = [expression for current_value in range(x,y)]
      print(variable_name)
'''

squares = [value**2 for value in range(1,11)]
print(squares)