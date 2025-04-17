###############################################################################
#   Damani Holland
#   4/3/2025
#   CS Python 121
###############################################################################

'''
Lists typically store values of the same data type,
they can also store values  of many different data types using brackets.
'''

c = [-45, 6, 0, 72, 1543]

print(c)

'''
Accessing Elements of a list
'''

print(c[0])

print(c[4])
'''
write the list name followed by the elements index enclosed in square brackets
'''

'''
Determine a list's length
Uses built-in function 'len()'
'''
print(len(c))

'''
Accessing Elements from the End of the List with Negative Indices
'''
print(c[-1])
print(c[-5])

'''
Indices Must Be Integers or Integer Expressions 
'''
a = 1
b = 2

print(c[a + b])

'''
List elements can be modified
'''

c[4] = 17
print(c)

'''
Some Sequences Are Immutable, and can not be modified
Python's string and tuple sequences are immutable
'''

s = 'hello'
print(s[0])

'''
Attempting to assign a new value to one of th characters causes a TypeError
-Remove (#) to see
'''
#s[0] = 'H'

'''
Attempting to Access a Nonexistent Element or out of range list, tuple, or string
index causes an IndexError
- remove (#) to see
'''
#print(c[100])

'''
Usig List Elements in Expressionss
-list elements may be used as variables in expressions
'''
print(c[0] + c[1] + c[2])

'''
Appendin to a list with +=
'''
a_list = []

for number in range(1, 6):
    a_list += [number]

print(a_list)

'''
You can append letters or string data as well
'''

letters = []

letters += 'Python'

print(letters)

'''
Concatenating lists with +
-You can concatenate two lists, two tuples or two strings
'''

list1 = [10, 20, 30]
list2 = [ 40, 50]

concatenated_list = list1 + list2

print(concatenated_list)

'''
Using for and range to Access List Indices and Values
'''
for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')

'''
Comparison Operators
- You can compare entire list element-by-element using comparison operators
'''
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]

print(a == b) 

print(a == c)

print(a < c)

print(c >= b)

'''
5.2 Exercise 3
'''

def cube_list(x):
    for i in range(len(x)):
        x[i] **= 3
        
exercise_list = []

for x in range(1, 11):
    exercise_list += [x]
    
cube_list(exercise_list)
print(exercise_list)


'''
5.2 exercise 4
'''

characters = []

characters += 'Birthday'

print(characters)