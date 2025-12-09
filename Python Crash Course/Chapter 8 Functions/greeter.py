###############################################################################
#   Damani Holland
#   12/06/2025
#   CS Python
###############################################################################

# Functions

'''
Functions:

    - Named blocks of code that are designed to do one specific job.
      When you want to perform a particular task that you've defined 
      in a function, you 'call' the name of the function responsible for it. 
'''

    # Use 'def' create a function assigned to name 'greet_user"
        # Print string statements
def greet_user():
    
    print("Hello!")
    
    # call function by name 'greet_user'
    
greet_user()

# Passing Information to a Function

    # Use 'def' to create function that takes an argument 'username'
        # print string statement with 'username' argument
def greet_user(username):
    print("Hello, " + username.title() + "!")

    # call function with string statement 'jesse' for the argument
greet_user('jesse')

# Arguments and Parameters

'''

Argument:

    - A oiece of information that is passed from a function call to a function.
    

Parameter:

    - A piece of information the function needs to do its job.
    
'''