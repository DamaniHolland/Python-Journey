###############################################################################
#   Damani Holland
#   4/9/2025
#   CS Python 121
###############################################################################
# 5.18 Exercises 5.4

'''
Create a 2-by-3 list, then use a nested loop to:
a) Set each element’s value to an integer indicating the order in which it was processed
by the nested loop.
b) Display the elements in tabular format. Use the column indices as headings
across the top, and the row indices to the left of each row.
'''

t = [[10, 7, 3], [20, 4, 17]]


for i, row in enumerate(t):
    for j, item in enumerate(row):
        print(f't[{i}][{j}] = {item}', end = ' ')
    print()
 
print('\nCreating a table for two dimensional list ', 't = ', (t))
print('\n')      
for index, item in enumerate(row):
    print(f'       Index #{index}', end='    ')

for i, row in enumerate(t):  
    print(f'\nRow #{i}')
    for j, item in enumerate(row):
        print(f'{item:>15}', end='    ')
        

# 5.18 Exercises 5.5

'''
Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz',
then perform the following separate slice operations to obtain:
a) The first half of the string using starting and ending indices.
b) The first half of the string using only the ending index.
c) The second half of the string using starting and ending indices.
d) The second half of the string using only the starting index.
e) Every second letter in the string starting with 'a'.
f) The entire string in reverse.
g) Every third letter of the string in reverse starting with 'z'.
'''
string = []
string += 'abcdefghijklmnopqrstuvwxyz'

print('\n a.) ',string[0:13])
print('\n b.) ',string[:13])
print('\n c.) ', string[13:26])
print('\n d.) ', string[13:])
print('\n e.) ', string[::2])
string.reverse()
print('\n f.) ', string)
print('\n g.) ', string[::3])

# 5.18 Exercises 5.6

'''
Define a function rotate that receives three arguments
and returns a tuple in which the first argument is at index 1, the second argument
is at index 2 and the third argument is at index 0. Define variables a, b and c containing
'Doug', 22 and 1984. Then call the function three times. For each call, unpack its result
into a, b and c, then display their values
'''
def rotate(arg):
    c, a, b = arg
    tuple = (a, b, c)
    print(tuple)
    return tuple

tuple = ('Doug', 22, 1984)
call1 = rotate(tuple)
call2 = rotate(call1)
call3 = rotate(call2)

# 5.18 Exercises 5.7

'''
Create a function that receives a list and returns a (possibly
shorter) list containing only the unique values in sorted order. Test your function with
a list of numbers and a list of strings.
'''
import numpy as np
import random

def unique(arg):
    values, frequencies = np.unique(arg, return_counts = True)
    return values

list1 = []
list2 = ['cat', 'dog', 'frog', 'rabbit', 'cat', 'goldfish', 'dog', 'guinea pig']
for i in range(1, 11):
    list1 += [random.randrange(1, 11)]
    
print(unique(list1))

# 5.18 Exercises 5.8

'''
A prime number is an integer greater than 1 that’s evenly
divisible only by itself and 1. The Sieve of Eratosthenes is an elegant, straightforward
method of finding prime numbers. The process for finding all primes less than 1000 is:
a) Create a 1000-element list primes with all elements initialized to True. List elements
with prime indices (like 2, 3, 5, 7, 11, …) will remain True. All other
list elements will eventually be set to False.
b) Starting with index 2, if a given element is True iterate through the rest of the
list and set to False every element in primes whose index is a multiple of the
index for the element we’re currently processing. For list index 2, all elements
beyond element 2 in the list that have indices which are multiples of 2 (i.e., 4,
6, 8, 10, …, 998) will be set to False.
c) Repeat Step (b) for the next True element. For list index 3 (which was initialized
to True), all elements beyond element 3 in the list that have indices which
are multiples of 3 (i.e., 6, 9, 12, 15, …, 999) will be set to False; and so on. A
subtle observation (think about why this is true): The square root of 999 is
31.6, you’ll need to test and set to False only all multiples of 2, 3, 5, 7, 9, 11,
13, 17, 19, 23, 29 and 31. This will significantly improve the performance of
your algorithm, especially if you decide to look for large prime numbers.
'''

primes = [True] * 10
# prime_list = [item for item in range(1, 1000)]

    
print(list(map(lambda index, value="False": value == "True",
               filter(lambda x: x % 2 == 0, (index for index, value in enumerate(primes[2:]))))))
