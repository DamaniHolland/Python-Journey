###############################################################################
#   Damani Holland
#   12/02/2025
#   CS Python
###############################################################################

'''

7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches . Then make an empty list called finished_sandwiches . Loop 
through the list of sandwich orders and print a message for each order, such 
as I made your tuna sandwich. As each sandwich is made, move it to the list 
of finished sandwiches . After all the sandwiches have been made, print a 
message listing each sandwich that was made.

'''

sandwiches = ['ham and cheese', 'turkey w/ sourdough', 'grilled cheese', 'sausage and egg']

finished_sandwiches = []

for sandwich in sandwiches:
    print("I have finished your " + sandwich.title() + " sandwich.")
    
    finished_sandwiches.append(sandwich)
    
print("\nfinished sandwiches: ")
for sandwich in sandwiches:
    print("\n\t" + sandwich)

