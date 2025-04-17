###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# List Comprehensions

list1 = []

for item in range(1, 6):
    list1.append(item)
    
print(list1)

# Using a List Comprehension to Create a List of Integers

'''
We can accomplish the same results as above with a single line of code
'''

list2 = [item for item in range(1, 6)]

print(list2)

# Mapping: Performing Operationg in a List Comprehension's Expression

'''
List Comprehension's Expression can perform taskss, such as calculations, that
map elelments to new values
'''

list3 = [item ** 3 for item in range(1, 6)]

print(list3)

# Filtering: List Comprehensions with 'if' Clauses

'''
'If' filters elements to select only those that match a condition
'''

list4 = [item for item in range(1, 11) if item % 2 == 0] # should only print even numbers

print(list4)

# List Comprehension That Processes Another List's Elements

colors = ['red', 'orange', 'yellow', 'green', 'blue']

colors2 = [item.upper() for item in colors] # note it applied a method to a whole iterable list

print(colors2)
print(colors)

# 5.12 Exercise 3

'''
Use a list comprehension to create a list of tuples containing the
numbers 1–5 and their cubes—that is, [(1, 1), (2, 8), (3, 27), …]. To create tuples,
place parentheses around the expression to the left of the list comprehension’s for clause.
'''

exercise_list = [(item, item ** 3) for item in range(1, 6)]

print(exercise_list)

# 5.12 Exercise 4

'''
Use a list comprehension and the range function with a step to create
a list of the multiples of 3 that are less than 30.
'''

exercise_list1 = [item for item in range(1, 30) if item % 3 == 0]

print(exercise_list1)