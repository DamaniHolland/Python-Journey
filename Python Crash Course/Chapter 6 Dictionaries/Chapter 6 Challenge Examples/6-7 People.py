###############################################################################
#   Damani Holland
#   11/22/2025
#   CS Python
###############################################################################


'''

6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) . 
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people . Loop through your list of people . As you 
loop through the list, print everything you know about each person

'''

users = {'amiri': {'first_name': 'amiri', 
        'last_name': 'aje', 
        'birth_date': '06-22-1998',
        'city': 'los angeles'
        }, 
        'damani': {'first_name': 'damani',
        'last_name': 'holland',
        'birth_date': '07-05-1998',
        'city': 'los angeles'},
}
for user in users:
    print(user + ": " + str(users[user]).title())