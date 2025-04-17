###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

# 5.8 Searching Sequences

'''
List Method index takes a search key which is the value to locate in the list, 
then searches through the list from index 0 and returns the index of the first 
element that matches the search key
'''
import random
numbers = [5, 7]
for i in range(1, 11):
    numbers.append((random.randrange(1, 11)))
print(numbers)

for index, value in enumerate(numbers):
    print(f'Index: {index}, Value:  {value}')
    
print(numbers.index(5)) # if 5 is not in the list it will cause a ValueError

'''
Specifying the Starting Index of a Search
'.index(search_key, starting search index, (x))'
'''

numbers *= 2 # creates two copies of the list

print(numbers)
print(numbers.index(5, 7)) # Searches for 5 starting from the 7th index in the list

'''
Specifying the starting and ending indices of a search
'.index(y, z, ending search index)
'''

print(numbers.index(7, 0, 4)) # If 7 is not found in the list just refresh the terminal

'''
Operators in and not in
Operator in  test whether the value on the left is contained inside the 
iterable on the right
'''

print(1000 in numbers)
print(5 in numbers)

'''
Operator no in tests whether the value on the left is not contained inside
the iterable on the right
'''

print(1000 not in numbers)
print(5 not in numbers)

'''
Using Operator in to Prevent a ValueError
a simple if else statement to print an error statement instead of breaking 
terminal
'''

key = 1000

if key in numbers:
    print(f'found {key} at index {numbers.index(search_key)}')
else:
    print(f'{key} not found')
    
# 5.9 Exercise 3

'''
Create a five-element list containing 67, 12, 46, 43 and 13, then
use list method index to search for a 43 and 44. Ensure that no ValueError occurs when
searching for 44.
'''
list = [67, 12, 46, 43, 13]

search_key = [43, 44]

for i in search_key:
    if i in list:
        print(f' found {i} at index {list.index(i)}')
    else:
        print(f'{i} not found')
    
