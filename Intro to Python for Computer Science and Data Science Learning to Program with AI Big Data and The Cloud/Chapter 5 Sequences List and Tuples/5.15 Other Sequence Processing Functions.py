###############################################################################
#   Damani Holland
#   4/9/2025
#   CS Python 121
###############################################################################

# Other Sequence Processin Functions

# Finding the Minimum and Maximum Values Using  a Key Function

'''
following statement is true due to the strings being compared by ord #'
'''
print('Red' < 'orange')

print(ord('R'))

print(ord('o'))

colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']

print(min(colors, key = lambda s: s.lower()))

print(max(colors, key = lambda s: s.lower()))

# Iterating Backwards Through a Sequence

'''
'reversed' returns an iterator that enables you to iterate over a sequence's
value backwards
'''
numbers = [10,3, 7, 1, 9, 4, 2, 8, 5, 6]

reversed_numbers = [item for item in reversed(numbers)]

print(reversed_numbers)

# Combining Iterables into Tuples of Corresponding Element

'''
'zip()' enables you to iterate over multiple iterables at the same time.
'''

names = ['Bob', 'Sue', 'Amanda']

grade_point_averages = [3.5, 4.0, 3.75]

for name, gpa in zip(names, grade_point_averages):
    print(f'Name = {name}; GPA = {gpa}')
    
# 5.15 Exercise 3

'''Create the list foods containing 'Cookies', 'pizza', 'Grapes',
'apples', 'steak' and 'Bacon'. Find the smallest string with min, then reimplement the
min call using the key function to ignore the strings’ case. Do you get the same results?
Why or why not?
'''
foods = ['Cookies', 'pizza', 'grapes', 'apples', 'steak', 'Bacon']

print(min(foods))

print(min(foods, key = lambda s: s.lower()))

# 5.15 Exercise 4

'''
Use zip with two integer lists to create a new list containing the sum
of the elements from corresponding indices in both lists (that is, add the elements at index
0, add the elements at index 1, …).
'''
import random
list1 = []
list2 = []
for i in range(1, 4):
     list1.append(random.randrange(1, 101))
    
print(list1) 

for i in range (1, 4):
    list2.append(random.randrange(1, 101))
    
print(list2)

list3 = [(a + b) for a, b in zip(list1, list2)]
print(list3)
