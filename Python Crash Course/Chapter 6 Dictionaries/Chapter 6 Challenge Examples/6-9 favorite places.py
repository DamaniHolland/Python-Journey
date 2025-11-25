###############################################################################
#   Damani Holland
#   11/25/2025
#   CS Python
###############################################################################

'''

6-9. Favorite Places: Make a dictionary called favorite_places . Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person . To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places . Loop through the dictionary, and print 
each person’s name and their favorite places

'''

favorite_places = {'ash': {'japan', 'los angeles', 'big bear'}, 
                   'autumn': {'japan', 'ireland', 'london'},
                   'damani': {'hawaii', 'egypt', 'ireland'}
    
}

for friend, favorite_places in favorite_places.items():
    print("\nName: ")
    print("\t" + friend.title())
    print("\nFavorite places they have visited:")
    print("\n\t" + str(favorite_places).title())