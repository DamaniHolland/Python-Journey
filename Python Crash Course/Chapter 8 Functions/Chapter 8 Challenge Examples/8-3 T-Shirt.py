###############################################################################
#   Damani Holland
#   12/08/2025
#   CS Python
###############################################################################

'''

8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt . The function should print 
a sentence summarizing the size of the shirt and the message printed on it .Call 
the function once using positional arguments to make a shirt . Call the function 
a second time using keyword arguments

'''

def make_shirt():
    size = input("what size T-shirt would you like?"\
                 "\nenter 'small', 'medium', or 'large': ")
    design = input("What would you like the shirt to say?"\
                   "\nEnter message here: ")

    print("The shirt size selected is a " + size + ". " + 
          "\nThe design for the shirt will say: " + design + ".")
    
make_shirt()