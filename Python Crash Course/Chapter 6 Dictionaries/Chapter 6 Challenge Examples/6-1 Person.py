###############################################################################
#   Damani Holland
#   11/18/2025
#   CS Python
###############################################################################


'''

6-1. Person: Use a dictionary to store information about a person you know . 
Store their first name, last name, age, and the city in which they live . You 
should have keys such as first_name, last_name, age, and city . Print each 
piece of information stored in your dictionary

'''

users = {'first_name': 'amiri', 
        'last_name': 'aje', 
        'birth_date': '06-22-1998',
        'city': 'los angeles'
        }
for user in users:
    print(user + ": " + users[user].title())