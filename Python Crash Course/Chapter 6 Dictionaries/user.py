###############################################################################
#   Damani Holland
#   11/19/2025
#   CS Python
###############################################################################

# Looping Through a Dictionary

'''

Looping Through All Key-Value Pairs

'''
    # A dictionary that contains one person's username, first name, 
    # and last name.
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

    # Create a list[] assinged(=) to variable 'friends'
        # list contains two items 'phil' and 'sarah
friends = ['phil', 'sarah']

    # Created a for loop by using 'for',
    # Created two variables to hold key value pairs 'username: efermi'
    # named 'key' and ' value.
    # called dictionary variable name 'user_0' 
    # Used .items() method, which returns a list of key-values as pairs.
    # Assinged for loop to every item in user_0 using 'in' method

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
    
    # Created a 'for' loop to find 