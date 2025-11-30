###############################################################################
#   Damani Holland
#   11/27/2025
#   CS Python
###############################################################################


'''

7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
that do each of the following at least once:

•  Use a conditional test in the while statement to stop the loop .

•  Use an active variable to control how long the loop runs .

•  Use a break statement to exit the loop when the user enters a 'quit' value

'''

# Program 1

'''
active = True
chosen_pizza_toppings = []
while active:
    what_pizza_toppings = 'What pizza toppings would you like to add: '
    what_pizza_toppings +=  "\nEnter 'quit' to quit program. "
    
    pizza_topping = input(what_pizza_toppings)
    
    
    if pizza_topping == 'quit':
        active = False
    else:
        print(pizza_topping.title() + " will be added to your pizza.")

'''

# program 2

'''
what_pizza_toppings = 'What pizza toppings would you like to add: '
what_pizza_toppings += '\nYou can input up to five toppings. '
topping_count = 0   

chosen_pizza_toppings = []
while topping_count <= 4:
    pizza_topping = input(what_pizza_toppings)
    chosen_pizza_toppings.append(pizza_topping)
    topping_count += 1
    
    if pizza_topping == 'quit':
        break
print("your toppings: " + chosen_pizza_toppings)
'''
