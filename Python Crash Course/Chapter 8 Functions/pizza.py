###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################

# Passing an Arbitrary Number of Arguments

    # create function 'make_pizza' with one argument '*toppings'
        # The '*' lets you pass as many arguments as you want in the call line

        # Display '*toppings'
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
    # call function 'make_pizza' with one argument 'pepperoni'
make_pizza('pepperoni')

    # call function 'make_pizza' with three arguments 'mushrooms', 
    # 'green peppers', 'extra cheese'
make_pizza('mushrooms', 'green peppers', 'extra cheese')


    # create function 'make_pizza' with one argument '*toppings'
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    
    # display string statement
    print("\nMaking a pizza with the following toppings:")
    
    # for every item 'topping' in arguments 'toppings'
        # display string statement with argument
    for topping in toppings:
        print("- " + topping)

    # call function 'make_pizza' with one argument     
make_pizza('pepperoni')

    # call function 'make_pizza' with three arguments
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments

    # create function 'make_pizza' with two arguments 'size, and '*toppings'
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    
    # display string statement with 'size' argument
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    
    # for every item 'topping' in argument(s) '*toppings'
        # display item 'topping'
    for topping in toppings:
        print("- " + topping)
        

    # call function with  two arguments '16', and 'pepperoni'             
make_pizza(16, 'pepperoni')

    # call function with four arguments '12', 'mushrooms', 'green peppers', 
    # 'extra cheese'
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

