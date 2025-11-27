###############################################################################
#   Damani Holland
#   11/27/2025
#   CS Python
###############################################################################


'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value . As they enter each topping, 
print a message saying you’ll add that topping to their pizza
'''
active = True
chosen_pizza_toppings = []
while active == True:
    what_pizza_toppings = 'What pizza toppings would you like to add: '
    what_pizza_toppings +=  "\nEnter 'quit' to quit program. "
    
    pizza_topping = input(what_pizza_toppings)
    
    if pizza_topping == 'quit':
        break
    else:
        print(pizza_topping.title() + " will be added to your pizza.")
        