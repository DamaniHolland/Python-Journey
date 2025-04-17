###############################################################################
#   Damani Holland
#   4/9/2025
#   CS Python 121
###############################################################################

# Two-Dimensional Lists

'''
List that require two indices to identify an element are called two-dimensional
list (or double-indexed lists or double-scripted lists). Typical use of such 
nested lists is to represent rables of values consisting of information arranged
in rows and columns
'''

# Creating Two-Dimensional List

'''
The following represents a table with 3 rows and 4 coulmns
'''

a = [[77, 68, 86, 73],  # First student's grades
     [96, 87, 89, 81],  # Second Student's grades
     [70, 90, 86, 81]]  # Third student's grades

'''
A list with m rows and n columns is called an 'm-by-n list and has m x n elements
'''

for row in a:
    for item in row:
        print(item, end=' ')
    print()
    
# How the Nested Loops Execute

for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}] = {item} ', end=' ')
    print()
    
# 5.16 Exercise 4

'''
Given the two-by-three integer list t
t = [[10, 7, 3], [20, 4, 17]]
a) Determine and display the average of t’s elements using nested for statements to
iterate through the elements.
b) Write a for statement that determines and displays the average of t’s elements using
the reductions sum and len to calculate the sum of each row’s elements and the
number of elements in each row.
'''

t = [[10, 7, 3], [20, 4, 17]]

total = 0

for row in t:
    for item in row:
        total += item

average = total / (len(t[0]) + len(t[1]))

print(average)