###############################################################################
#   Damani Holland
#   11/29/2025
#   CS Python
###############################################################################

# Moving Items from One List and Dictionaries

    # Moving Items from One List to Another

    # a list of unconfirmed users in a list assigned to 'unconfirmed_users'
    # assign empty list to 'confirmed_users'
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

    # while using values in unconfirmed_users
        # removes current value from list unconfirmed_users[] 
        # assign to variable current_user
        # print 'verifying user: current_user
        # add current_user value to empty list confirmed_users[]
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

    # print string statement
    # for every value in confirmed_users list
    # print confirmed_user value
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
