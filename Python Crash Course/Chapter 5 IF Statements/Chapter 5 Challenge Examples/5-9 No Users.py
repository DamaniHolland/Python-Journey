###############################################################################
#   Damani Holland
#   11/17/2025
#   CS Python
###############################################################################


'''

5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
not empty .

•  If the list is empty, print the message We need to find some users!

•  Remove all of the usernames from your list, and make sure the correct 
message is printed

'''

usernames = ['employee_1', 'employee_2', 'employee_3', 'employee_4', 'admin']

for username in usernames:
    if username == 'admin':
        print("Hello " + username + ", Would you like to check the daily report?")
    else:
        print("Hello " + username + ", thank you for logging in.")

# Checking for empty list

usernames = []

if usernames == []:
    print("We need to find some users. ASAP!")

for username in usernames:
    if username == 'admin':
        print("Hello " + username + ", Would you like to check the daily report?")
    else:
        print("Hello " + username + ", thank you for logging in.")
