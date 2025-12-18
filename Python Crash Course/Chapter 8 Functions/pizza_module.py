###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################

# Storing your Functions in Modules

'''

Modules:

    - A seperate file that stores functions, whoch are then imported into
        another file.
        
'''

    # Importing an entire Module
    
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
    # Importing Specific Functions
    
'''

Syntax:

    -from module_name import function_name
    
'''
        
