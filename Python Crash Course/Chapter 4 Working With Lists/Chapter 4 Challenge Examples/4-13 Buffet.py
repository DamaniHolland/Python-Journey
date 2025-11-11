###############################################################################
#   Damani Holland
#   11/09/2025
#   CS Python
###############################################################################

'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five 
simple foods, and store them in a tuple .

•  Use a for loop to print each food the restaurant offers .

•  Try to modify one of the items, and make sure that Python rejects the 
change .

•  The restaurant changes its menu, replacing two of the items with different 
foods . Add a block of code that rewrites the tuple, and then use a for 
loop to print each of the items on the revised menu .
'''

meat_lovers_buffet = ("garlic chicken", "lamb chop", "wagyuu beef", "brisket", "pork chop")

print("\nOriginal menu items are:")
for meat in meat_lovers_buffet:
    print(meat)
    
# meat_lovers_buffet[0] = "chicken strips"

meat_lovers_buffet = ("garlic chicken", "lamb chop", "wagyuu beef", "smoked salmon", "poke")
print("\nModified menu are:")
for meat in meat_lovers_buffet:
    print(meat)