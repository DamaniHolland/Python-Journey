###############################################################################
#   Damani Holland
#   11/11/2025
#   CS Python
###############################################################################

answer = 17 

if answer != 42:
    print("This is not the correct answer. please try again!")
    
'''
Using 'and' to check multiple Conditions
'''

age_0 = 22
age_1 = 18

'''
Numerical Comparisons can also be made with the following Syntax

- ==
- !=
- >
- <
- >=
- <=

Using 'and' allows you to compare multiple conditions at the same time.

Syntax:

    - if variable_1 == to element and variable_2 == to element:
            print(element)
            
Both statements must be true before the code indented underneath is executed
'''

if age_0 >= 21 and age_1 >= 21:
    print("true")
else:
    print("false")
    
'''
Using 'or' to Check Multiple Conditions

Syntax:

    - if variable_1 == to element or variable_2 == to element:
            print(element)

Only one of these statements must be true in order to execute the indented 
code underneath
'''

age_0 = 22
age_1 = 18

if age_0 >= 21 or age_1 >= 21:
    print("True")
else:
    print("False")

