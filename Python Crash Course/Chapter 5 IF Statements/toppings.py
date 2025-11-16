###############################################################################
#   Damani Holland
#   11/11/2025
#   CS Python
###############################################################################

# If Stamements

'''
Checking for Inequality

Syntax: 

    - if variable != element
          print(element)
          
- The (!=) helps to check for inequality where if the if statement is fufilled
  then it runs the next indented line of code underneath.
'''

requested_topping = ['mushroom', 'onion', 'pineapple']

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
'''
Checking whether a Value Is in a List

Syntax:

    - element in list_variable_name
'''

print('mushroom' in requested_topping)
print('pepperoni' in requested_topping)

# Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!")

# Using if Statements with Lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")