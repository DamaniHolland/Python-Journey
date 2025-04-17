###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# Generator Expressions

'''
A generaator expression is similar to a list comprehension, but creates and 
iterable generator object that produces values on demand. Generator Expressions
have the same capabilities as list comprehensions, but you define them in 
parentheses instead of square brackets.
'''

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')
    
square_of_odds = (x ** 2 for x in numbers if x % 2 != 0)

print(square_of_odds)

# 5.13 Exercise 2

'''
Create a generator expression that cubes the even integers in a list
containing 10, 3, 7, 1, 9, 4 and 2. Use function list to create a list of the results. Note
that the function call’s parentheses also act as the generator expression’s parentheses.
'''

print(list(x ** 3 for x in numbers[:7] if x % 2 == 0))
