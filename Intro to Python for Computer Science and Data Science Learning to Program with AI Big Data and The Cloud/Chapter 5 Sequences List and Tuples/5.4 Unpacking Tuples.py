###############################################################################
#   Damani Holland
#   4/4/2025
#   CS Python 121
###############################################################################

# Unpacking Sequences

'''
you can unnpack any sequences elements by assigning the sequence to any list of
variables.
'''
student_tuple = ('Amanda', [98, 85, 87])
first_name, grades = student_tuple # Unpacks elements in a sequqnece

print(first_name)
print(grades)

'''
A ValueError occurs if the number of variables to the left of the assignment 
('first_name, grades'(2)) is not identical to the number of elements in the
sequence on the right ('Amanda', [98, 85, 87](2)) 
'''

'''
The following code unpacks a string, a list, and a sequence produced by range:
'''

first, second = 'hi'
print(f'{first}  {second}')

number1, number2, number3 = [2, 3, 5]

print(f'{number1}   {number2}   {number3}')

number1, number2, number3 = range(10, 40, 10)
print(f'{number1}   {number2}   {number3}')

'''
Swapping variables using packing and unpacking
'''

number1 = 99
number2 = 22

number1, number2 = (number2, number1)

'''
Notice the values have been swapped, number2's value is now number1's original
and number1's value is now number2's original value
'''
print(f'number1 = {number1}: number2 = {number2}')

'''
Accessing indices and values using built-in function enumerate
'''

colors = ['red', 'orange', 'yellow']

print(list(enumerate(colors))) #enumerate creates a tuple containing the index 
                               #and its value
                               
print(tuple(enumerate(colors)))

'''
The following takes results from enumerate(colors) and prints in tabular format
'''
for index, value in enumerate(colors):
    print(f'{index}: {value}')
    
'''
The following code takes a list of values and displays a simple bar chart
'''
import random

numbers = []

for i in range(1, 11):
    numbers.append(random.randrange(1, 101))

print('\ncreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}    {'#' * value}')
          
# 5.4 Exercise 3

'''
Create a tuple high_low representing a day of the week (a string)
and its high and low temperatures (integers), display its string representation, then perform
the following tasks in an interactive IPython session:
a) Use the [] operator to access and display the high_low tuple’s elements.
b) Unpack the high_low tuple into the variables day and high. What happens and
why?
'''
high_low = ('Saturday', 78, 50)
day_of_week, temp_high, temp_low = high_low

print(f'Today is {day_of_week}. The temperature high is going to be {temp_high} degrees, and the low will be {temp_low} degrees.')

print(list(enumerate(high_low)))

# 5.4 Exercise 4

'''
Create the list names containing three name strings. Use a for loop
and the enumerate function to iterate through the elements and display each element’s
index and value.
'''

names = ('Drake', 'Josh', 'Megan')

for i in range(len(names)): # uses (i) to obtain indices
    print(f'{i}: {names[i]} ')
    
for index, value in enumerate(names): # Uses enumerate to obtain indices
    print(f'{index}: {value}')