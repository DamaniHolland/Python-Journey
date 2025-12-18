###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################


'''

8-13. User Profile: Start with a copy of user_profile.py from page 153 . Build 
a profile of yourself by calling build_profile(), using your first and last names 
and three other key-value pairs that describe you

'''

def build_profile(first, last, **user_info):
    profile = {}
    
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
        
    return profile

user = build_profile('damani', 'holland', date_of_birth='07-05-98',
              birth_location='los angeles', current_location='culver city')

print(user)
