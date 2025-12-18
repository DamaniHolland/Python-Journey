###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################

'''

8-15. Printing Models: Put the functions for the example print_models.py in a 
separate file called printing_functions.py . Write an import statement at the top 
of print_models.py, and modify the file to use the imported functions.

'''

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
