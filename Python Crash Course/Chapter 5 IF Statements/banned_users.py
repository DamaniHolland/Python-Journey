###############################################################################
#   Damani Holland
#   11/11/2025
#   CS Python
###############################################################################

'''
Checking Whether a Value Is Not in a list

element not in list_variable_name

used to check if an element is not in a list using 'not in' as the conditional
'''

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")