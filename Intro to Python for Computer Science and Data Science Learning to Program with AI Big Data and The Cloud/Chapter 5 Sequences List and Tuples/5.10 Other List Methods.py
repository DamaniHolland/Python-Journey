###############################################################################
#   Damani Holland
#   4/5/2025
#   CS Python 121
###############################################################################

color_names = ['orange', 'yellow', 'green']
print(color_names)

# Inserting an Element at a specific List Index

'''
Method 'insert' adds a new item at a specified index.
'''

color_names.insert(0, 'red')

print(color_names)

# Adding an Element to the End of a List


'''
Method '.append()' adds a new item to the end of a list
'''
color_names.append('blue')

print(color_names)

# Adding All Elements of a Sequence to the End of a List

'''
Method '.extend()' adds all the elements of another sequence to the end of a list
'''

color_names.extend(['indigo', 'violet'])

print(color_names)

sample_list = []

s = 'abc'

sample_list.extend(s) # adds all string elements to sample_list

print(sample_list)

t = (1, 2, 3)

sample_list.extend(t) # adds all elements of tuple to sample_list

print(sample_list)

sample_list.extend((4, 5, 6)) # note the extra parentheses
                              # it accepts an entire tuple as an argument

print(sample_list)

# Removing the First Occurrence of an Element List

'''
Method '.remove()' deletes the first element with a specified value
ValueError occurs if argument is not in list
'''

color_names.remove('green')

print(color_names)

# Emptying a List

'''
Method '.clear()' deletes all the elements in a list
'''

color_names.clear()

print(color_names)

# Counting the Number of Occurrences of an Item

'''
List method '.count()' searches for its argument and returns the number of times 
it's found
'''

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3,
             1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times in responses')
    
# Reversing a List's Elements

'''
List method '.reverse()' reverses the contents of a list in place, rather than 
creating a reversed copy
'''

color_names = ['red', 'orange', 'yellow', 'green', 'blue']
print(color_names)

color_names.reverse() # reverses the orignal list assigned to the value

print(color_names)

# Copying a List

'''
List method '.copy()' returns a new list containing a shallow copy of the 
original list
'''

copied_list = color_names.copy()

print(copied_list)

# 5.3 Exercise 3

'''
Create a list called rainbow containing 'green', 'orange' and
'violet'. Perform the following operations consecutively using list methods and show
the list’s contents after each operation:
a) Determine the index of 'violet', then use it to insert 'red' before 'violet'.
b) Append 'yellow' to the end of the list.
c) Reverse the list’s elements.
d) Remove the element 'orange'.
'''

rainbow = ['green', 'orange', 'violet']

print(rainbow)

rainbow.insert(rainbow.index('violet'), 'red')

print(rainbow)

rainbow.append('yellow')

print(rainbow)

rainbow.reverse()

print(rainbow)

rainbow.remove('orange')

print(rainbow)