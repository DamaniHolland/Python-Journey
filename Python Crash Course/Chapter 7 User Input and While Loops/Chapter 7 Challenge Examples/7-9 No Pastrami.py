###############################################################################
#   Damani Holland
#   12/02/2025
#   CS Python
###############################################################################

'''

7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
the sandwich 'pastrami' appears in the list at least three times . Add code 
near the beginning of your program to print a message saying the deli has 
run out of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up 
in finished_sandwiches

'''

sandwiches = ['ham and cheese', 'pastrami', 'turkey w/ sourdough', 'pastrami',
               'grilled cheese', 'sausage and egg', 'pastrami']

finished_sandwiches = []

print("The deli has officially run out of 'pastrami' sandwiches")

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')
    
for sandwich in sandwiches:
    print("I have finished your " + sandwich.title() + " sandwich.")
    
    finished_sandwiches.append(sandwich)

print("\nfinished sandwiches: ")
for sandwich in sandwiches:
    print("\n\t" + sandwich)

