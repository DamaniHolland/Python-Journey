###############################################################################
#   Damani Holland
#   11/09/2025
#   CS Python
###############################################################################

# Tuples

'''
Immutable: values that cannot change.
Tuples: an immutable list

Syntax:

    - variable_name = (tuple, items)
    
Tuples use parenthesis() to contain items instead of square brackets[].
'''

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

'''
If we try to change any item in the tuple we will get an error
'''
# dimensions[0] = 250

'''
Looping Through All Values in a Tuple
'''

for dimension in dimensions:
    print(dimension)

'''
Writing over a Tuple
'''

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)