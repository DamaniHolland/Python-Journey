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