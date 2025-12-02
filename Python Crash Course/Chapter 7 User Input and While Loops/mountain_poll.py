###############################################################################
#   Damani Holland
#   12/01/2025
#   CS Python
###############################################################################

# Filling a Dictionary with User Input


    # create dictionary assigned to variable 'responses'
responses = {}

    # set 'True' to variable 'polling_active'
polling_active = True

    # While active variable set to True
        # set user input function to variable 'name'
        # set another user input function to variable 'response'
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
        # assign a set value pair 'name': 'response' to dictionary 'responses'
    responses[name] = response
    
        # assign user input function to variable 'repeat'
    repeat = input("Would you like to let another person respond? (yes/ no)")
       
        # if repeat is 'no'
            # set active variable 'polling_active' to 'False'
    if repeat == 'no':
        polling_active = False

    # print string statement       
print("\n--- Poll Results ---")

    # for key-value pairs 'name', 'response' in dictionary 'responses'
        # print key 'name' and value 'response' to string statement
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
                   
    
