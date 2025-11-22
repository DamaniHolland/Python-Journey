###############################################################################
#   Damani Holland
#   11/21/2025
#   CS Python
###############################################################################


'''
6-6. Polling: Use the code in favorite_languages.py (page 104) .

•  Make a list of people who should take the favorite languages poll . Include 
some names that are already in the dictionary and some that are not . 

•  Loop through the list of people who should take the poll . If they have 
already taken the poll, print a message thanking them for responding . 
If they have not yet taken the poll, print a message inviting them to take 
the poll .

'''

favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python'
    }
    
    # Create a list[] assinged(=) to variable 'friends'
        # list contains two items 'phil' and 'sarah

friends = ['phil', 'sarah']

need_to_take_poll = ['jake', 'sally', 'phil', 'edward', 'hank']

for name in need_to_take_poll:
    if name not in favorite_languages.keys():
        print(name.title() + ', please take the poll so we can discover which ' 
              'language people like most. Thank You!')
    else:
        print(name.title() + ' Thank you for voting :D!')

 