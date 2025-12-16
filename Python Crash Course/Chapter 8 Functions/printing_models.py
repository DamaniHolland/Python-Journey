###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################

# Modifying a List in a Function

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
    
###############################################################################
print("###############################################################################")

    # create function 'print_models' with two arguments 'unprinted design', 
    # 'completed_models'
    
   
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed models after printing.
    """
     # while 'unprinted_designs' has values:
        # create variable 'current_design' is assigned to value of 'unprinted_designs'
        # with '.pop()' method
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # simulate creating a 3D print from the design
            # display string statement with 'current_design'
            # add 'current_design' to end of list 'completed_models' with 
            # '.append()' method
        print("Printing model: " + current_design)
        completed_models.append(current_design)
    
    # create function 'show_completed_models' with argument 'completed_models'
def show_completed_models(completed_models):
    """Show all models that were printed."""
    
        # display string statement
    print("\nThe following models have been printed:")
    
        # for every item 'completed_model' in list 'completed_models'
            # display item 'completed_model'
    for completed_model in completed_models:
        print(completed_model)
        
    # create variable 'unprinted_designs' and assign it to a list with 3 items
    # create variable 'completed_models' and assign it to empty list
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

    # call function 'print_models' with two arguments 'unprinted_designs', 'completed_models'
    # call function 'show_completed_models' with one argument 'completed_models'
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)