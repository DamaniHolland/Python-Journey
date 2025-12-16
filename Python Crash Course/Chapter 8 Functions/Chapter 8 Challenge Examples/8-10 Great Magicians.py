###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################

'''

8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 . 
Write a function called make_great() that modifies the list of magicians by add-
ing the phrase the Great to each magician’s name . Call show_magicians() to 
see that the list has actually been modified

'''
magicians = ['imani', 'leo', 'autumn']

def make_great(list):
    for name in magicians:
        name = 'The Great ' + name.title()
        print(name)
        
make_great(magicians)