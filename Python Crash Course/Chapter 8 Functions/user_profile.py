###############################################################################
#   Damani Holland
#   12/15/2025
#   CS Python
###############################################################################

# Using Arbitrary Keyword Arguments

    # create function 'build_profile' with 3 arguments 
    # 'first', 'last', '**user_info' the double asterisk creates an empty dictionary

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we everything we know about a user."""
    
        # create dictionary named 'profile'
    profile = {}
        # Add key-value 'first_name': 'albert' to dictionary 'profile'
    profile['first_name'] = first
    
        # Add key-value 'last_name': 'einstein' to dictionary 'profile'
    profile['last_name'] = last
    
        # for every key-value pair in dictionary 'user_info'
            # create key_value pair to add to dictionary 'profile'
            
    for key, value in user_info.items():
        profile[key] = value
        
        # return dictionary 'profile
    return profile

    # variable 'user_profile' assigned to function 'buuld_profile' with arguments:
    # 'albert', 'einstein', key-value: 'location': 'princeton', 'field': 'physics'
user_profile = build_profile('albert', 'einstein', 
                             location='princeton', 
                             field='physics')

    # display variable user profile
print(user_profile)