###############################################################################
#   Damani Holland
#   12/12/2025
#   CS Python
###############################################################################

'''

8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python . Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message

'''

def make_shirt(shirt_size='large', design='I love Python'):

    print("The shirt size selected is a " + shirt_size.title() + ". " + 
          "\nThe design for the shirt will say: " + design + ".")
    
make_shirt('medium')
make_shirt('small', 'I will land a job')

    