###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################


'''

8-9. Magicians: Make a list of magician’s names . Pass the list to a function 
called show_magicians(), which prints the name of each magician in the list

'''

magicians = ['imani', 'leo', 'autumn']

def show_magicians(magicians):
    for magician in magicians:
        print("revealing magician: " + magician.title())
        
show_magicians(magicians)