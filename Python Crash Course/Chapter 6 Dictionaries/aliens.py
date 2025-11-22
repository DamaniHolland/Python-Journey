###############################################################################
#   Damani Holland
#   11/21/2025
#   CS Python
###############################################################################


# Nesting

    # created a dictionary holding attribute: information value pairs.
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

    # Stored dictionaries in a list called aliens
aliens =  [alien_0, alien_1, alien_2]

    # for every item in aliens:
        # print dictionary 
for alien in aliens:
    print(alien)
print('\n'
      '######################################################################')

    # Created an empty list to store dictionaries in
aliens = []

    # every number 0 - 30
        # Make a dictionary and assign it 'attributes': 'values' to variable 
        # 'new_alien'.
        
        # Add 'new_alien' to end of list 'aliens'. 
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

    # for every alien in indexes 0 - 2:
        # if dictionary['attribute'] is the same as 'value'
            # Change dictionary['attribute'] to 'new_value'
        # elif dictionary['attribute'] is the same as 'value'
            # Change dictionary['attribute'] to 'new_value'
        
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

    # for every dictionary in indexes 0 - 4
        # print dictionary   
for alien in aliens[:5]:
    print(alien)
    
    # print string statement
print('...')

    # print total number of aliens with str(len(list))
print("total number of aliens: " + str(len(aliens)))