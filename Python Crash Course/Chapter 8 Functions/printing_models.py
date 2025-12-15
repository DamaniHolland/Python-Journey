###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################

# Start with some designs that need to be printed.

    # create list 'unprinted_design' and assign it to 3 items
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

    # create list 'completed_models' that is empty
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

    # create loop for going through list 'unprinted_designs'
        # create variable 'current_design' and assign it to 'unprinted_design'
        # with '.pop()' method to remove it from the 'unprinted_designs' list
        
        # Display string statement with value assigned to 'current_design'
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    
# Display all cmompleted models.
# Display string statement
# for every item 'completed_model' in list 'completed_models':
    # Display item'completed_model'
print("The folowing models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
