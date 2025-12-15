###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################

# Passing a List

    # create function 'greet_users' with one argument 'names'
        # for every item 'name' in list 'names'
            # create varaible 'msg' and store string message with 'name' with 
            # '.title()' method.

            # display 'msg'

def greet_users(names):
    "Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

    # create variable 'usernames' and assign it to list with 3 items    
usernames = ['hannah', 'ty', 'margot']

    # call function 'greet_users' with argument 'usernames'
greet_users(usernames)


