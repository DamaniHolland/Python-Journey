###############################################################################
#   Damani Holland
#   11/25/2025
#   CS Python
###############################################################################

# Using break to Exit a Loop

'''

Break Statement:
 
    - THe break statement directs the flow of your program; you can use it to 
      control which lines of code are executed and which aren't, so the program 
      only executes code that you want it to, when you want it to.
    
'''
    # prompt user to enter a string element
    # prompt user how to quit

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(enter 'quit' when you are finished.) "

    # while True
        # assign user input to city
        
        # if user input (city) is 'quit'
            # break
        
        # else
            # print statement with user input(city)
while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")