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