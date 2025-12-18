###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################


'''

8-12. Sandwiches: Write a function that accepts a list of items a person wants 
on a sandwich . The function should have one parameter that collects as many 
items as the function call provides, and it should print a summary of the sand-
wich that is being ordered . Call the function three times, using a different num-
ber of arguments each time.

'''

def make_sandwich(*sandwich_items):
    print("\n---Sandwich items include---")
    
    for item in sandwich_items:
        print("\n\t- " + item)
        
make_sandwich('lettuce', 'tomato', 'red onion', 'turkey')
make_sandwich('ham', 'cheese')
make_sandwich('peanut butter', 'banana', 'jelly')
        
        