###############################################################################
#   Damani Holland
#   11/22/2025
#   CS Python
###############################################################################

# Nesting

    # A Dictionary in a Dictionary

    # Created a dictionary{} to variable 'user' storing
        # 'name': {dictionary_of: attributes, 'first': 'name'}
user = {
    'aeinstein': {
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton',
    }, 
    'mcurie': {
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris',
    },
}

    # For every 'Key', 'Value' in dictionary('user') key-value pairs(.items())
        # print 'key'
        # assign values of keys 'first' and 'last' to variable full_name
        # assign variable 'location' to value of key 'location'
for username, user_info in user.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())