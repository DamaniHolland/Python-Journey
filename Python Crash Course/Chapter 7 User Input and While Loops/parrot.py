###############################################################################
#   Damani Holland
#   11/25/2025
#   CS Python
###############################################################################

# User Input and While Loops

'''

How the input() Function Works

    - The input() function pauses you program and waits for the user to enter
      some text.

Syntax:

    - variable = input("string of instructions")
'''

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Letting the User Choose When to Quit

    # instruct user to enter a string element
    # tells user how to quit the program
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "


'''
^
|
|
get rid of this to see code


    # assign message to blank string element
message = ""

    # while message is not equal to string element 'quit'
    # assign prompt strings to message
while message != 'quit':
    message = input(prompt)
    
    # if user input does not equal 'quit'
        # print user input
    if message != 'quit':
        print(message)

'''

# Using a Flag

'''
Flag

    - This variable, called a flag, acts as a signal to the program.
      We can write the program so it runs if the flag is set to 'True' and
      stop running when any of several events set the value of flag to 'False'.
'''

    # create a variable used as a flag for while loop and set to 'True'
active = True

    # While flag is set to 'True' 
    # user input is assigned to variable 'message'
while active:
    message = input(prompt)
    
    # if message is 'quit'
    # assign switch to 'false'
    if message == 'quit':
        active = False

    # else 
    # print input prompt    
    else:
        print(message)