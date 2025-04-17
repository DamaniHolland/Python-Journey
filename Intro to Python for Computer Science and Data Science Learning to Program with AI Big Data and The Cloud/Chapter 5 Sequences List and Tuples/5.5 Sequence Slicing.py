###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# 5.5 Sequence Slicing

'''
Specifying a Slice with Staring and Ending Indices
'''
import random

numbers = []

for i in range(1, 9):
    numbers.append(random.randrange(1, 21))

'''
The slice copies elements from the starting index to the left of the colon up
to, nut not including, the ending index to the right of the colon.

* The original list is not modified
'''
print(numbers)

# create slice
print(numbers [2:6]) # specified indices are 2 and 6

'''
Specifying a Slice with Only an Ending Index
'''
print(numbers[0:6]) # Slices from beginning to ending index

# Remove (#) to see
# print(numbers[:6]) # Same result as the one above 

'''
Specifying a Slice with Only a Starting Index
'''

print(numbers[6:]) # Slices from staring Index specified to end of sequence

print(numbers[6:len(numbers)])

'''
Specifying a Slice with No Indices
'''
numbers[:] # Slices / Copies the entire sequence

'''
Slicing with Steps
'''
print(numbers[::2]) # Uses a step of 2 to create a slice with every other element

'''
Slicing with Negative Indices and Steps
'''

print(numbers[::-1]) # selects slices in reverse order

# Remove (#) to see
# print(numbers[-1: -9: -1]) # Same as the code above

'''
Modifying Lists Via Slices
'''
'''
The following code replaces the first three elements of the sequence with 
'two', 'three' and 'five' while leaving the rest of the sequence unchanged.
'''
numbers[0:3] = ['two', 'three', 'five']

print(numbers)

'''
The following code deletes the list using an empty list
'''
numbers[:] = []

print(numbers)

'''
The following assigns a list's elements to a slice of every other elements of 
numbers
'''
for i in range(1, 9):
    numbers.append(random.randrange(1, 21))
print("new List: ", numbers)    

numbers[::2] = [100, 100, 100, 100]
print(numbers)

'''
The following code is just to demonstrate how even though the list sequence is
empty it is still the same list until we reassign it
'''
print(id(numbers))

numbers[:] = []
print(numbers)

print(id(numbers))

numbers = []
print(id(numbers))

# 5.5 Exercise 3

'''
Create a list called numbers containing the values from 1 through
15, then use slices to perform the following operations consecutively:
a) Select number’s even integers.
b) Replace the elements at indices 5 through 9 with 0s, then show the resulting list.
c) Keep only the first five elements, then show the resulting list.
d) Delete all the remaining elements by assigning to a slice. Show the resulting list.
'''

for i in range(1, 16):
    numbers.append(i)
    
print(numbers)
print(numbers[1::2])
numbers[5:10] = [0] * len(numbers[5:10])
print(numbers)
print(numbers[:5])
numbers[:] = []
print(numbers)