###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################

'''

8-11. Unchanged Magicians: Start with your work from Exercise 8-10 . Call the 
function make_great() with a copy of the list of magicians’ names . Because the 
original list will be unchanged, return the new list and store it in a separate list . 
Call show_magicians() with each list to show that you have one list of the origi-
nal names and one list with the Great added to each magician’s name .

'''

magicians = ['imani', 'leo', 'autumn']
great_magicians = []

def great_magician(magicians, great_magicians):
    
    for magician in magicians:
        current_magician = "The Great " + magician.title()
        great_magicians.append(current_magician)
        print(current_magician)
    
great_magician(magicians, great_magicians)
print(great_magicians)
print(magicians)