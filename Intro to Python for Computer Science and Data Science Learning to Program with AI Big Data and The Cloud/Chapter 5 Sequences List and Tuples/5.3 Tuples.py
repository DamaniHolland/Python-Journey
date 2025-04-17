###############################################################################
#   Damani Holland
#   4/3/2025
#   CS Python 121
###############################################################################

'''
Creating Tuples
- To create a tuple use parentheses instead of brackets
'''

student_tuple = ()

print(student_tuple)

print(len(student_tuple))

'''
You can pack tuples by seperating the values with commas
'''
student_tuple = 'John', 'Green', 3.3

print(student_tuple)
print(len(student_tuple))

'''
You may surround a tuple's comma seperated list of values with optional parentheses
'''
another_student_tuple = ('Mary', 'Red', 3.3)

print(another_student_tuple)

'''
The following creates a one element tuple
'''
a_singleton_tuple = ('red',) # note the comma

print(a_singleton_tuple)

'''
Accessing Tuple Elements
usually tuples are meant to access the values individually rather than 
iterating over thembelow is an example of code meant to calculate how many 
second since midnight using (hour, minute, second) as values for our tuple
'''

time_tuple = (9, 16, 1)
print(time_tuple)

seconds_since_midnight = time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2]
print(seconds_since_midnight)

'''
Adding Items to a String or Tuple
'''

tuple1 = (10, 20, 30)

tuple2 = tuple1

print(tuple2)

'''
concatenating the tuple (40, 50) to tuple1 creates a new tuple while tuple2
still referes to original tuple
'''

tuple1 += (40, 50)

print(tuple1)

print(tuple2)

'''
For a string or tuple, any items to the right of += must be a sting or tuple, 
mixing types will cause a TypeError
'''

'''
Appending Tuples
- you can use += to append to a list
'''

numbers = [1, 2, 3, 4, 5]

numbers += (6, 7)

print(numbers)

'''
Tuples May Contain Mutable Objects
- Let's create a student_tuple with first name, last name and list of grades:
'''

student_tuple = ('Amanda', 'Blue', [98, 75, 87])

'''
Even though the tuple is immutable, its list elemets is mutable
We can replace the list item even though it is in the tuple simply by accessing the list 
'''
student_tuple[2][1] = 85
print(student_tuple)

'''
5.4 Exercise 3
'''
# Create a single-element tuple containing 123.45, then display it.

single = (123.45,)
print(single)

# Show what happens when you attempt to concatenate sequences of
# different types—the list [1, 2, 3] and the tuple (4, 5, 6)—using the + operator.

list = [1, 2, 3]
tuple = (4, 5, 6)

'''
A TypeError will appear since you can only concatenate list to list and not tuple to list
'''
# list + tuple