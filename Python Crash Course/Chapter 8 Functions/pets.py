###############################################################################
#   Damani Holland
#   12/08/2025
#   CS Python
###############################################################################

# Positional Arguements

    # Use 'def' to create a function that takes two arguments 'animal_type', 
    #'pet_name'
        # print string statments that use the arguments 
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
    # call function with arguments 'hamster, 'harry'
describe_pet('hamster', 'harry')
    
# Multiple Function Calls

describe_pet('dog', 'willie')

# Order Mattters in Positional Arguments

describe_pet('harry', 'hamster')
 
# Keyword Arguments

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values

    # sets a default value for the argument 'animal_type' being 'dog'
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name='willie')

# Equivalent Function Calls

    # A dog named Willie
describe_pet('Willie')
describe_pet(pet_name='Willie')

    # A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


    
