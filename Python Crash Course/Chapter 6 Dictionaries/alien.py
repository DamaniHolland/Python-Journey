###############################################################################
#   Damani Holland
#   11/18/2025
#   CS Python
###############################################################################

# A Simple Dictionary

'''

Syntax:

    - dictionary_variable = {keyword : value, keyword : value}
      print(dictionary_variable['keyword'])
'''

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print(alien_0['color'])
print(alien_0['points'])

# Adding New Key-Value Pairs

'''

Syntax:

    - dictionary_variable['new_keyword'] = new_value
    
'''

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying Value in a Dictionary

'''

Syntax:

    - dictionary_variable['keyword'] = new_value
    
'''
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original X-position: " + str(alien_0['x_position']))

    # Move the alien to the right.
    # Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

    # The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# Removing Key-Value Pairs

'''

Syntax:

    - del dictionary_variable['keyword']
    
'''

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

