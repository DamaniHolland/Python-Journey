###############################################################################
#   Damani Holland
#   11/09/2025
#   CS Python
###############################################################################

# Working with Part of a List

'''
Slicing a List

- Slice: a specific group of items in a list.

Syntax:

    - variable_name = [list, items]
      print(variable_name[x:y])
      
- You specify the start of the slice with 'x' and specify
    the end of slice with 'y'. The end stops one value short of what you specify
'''

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players)

print(players[0:3])

print(players[1:4])

'''
By omitting the first index in a slice you automatically start at the 
beginning of the list, same thing for omitting the last index which will 
automatically go to the end of the list.
'''
print(players[:4])

'''
if you want to recall and index a certain distance from the end of the list
you simply make the 'x' value negative(-x)
'''

print(players[-3:])

# Looping Through a Slice

'''
Using a slice to make a range for the loop to work through
'''

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
# Copying a List