###############################################################################
#   Damani Holland
#   11/08/2025
#   CS Python
###############################################################################

# 3-9 Dinner Guest
'''
If you could invite anyone, living or deceased, to dinner, who 
would you invite? Make a list that includes at least three people you’d like to 
invite to dinner. Then use your list to print a message to each person, inviting 
them to dinner
'''

guest_list = ['the creator', 'donald trump', 'isaac newton']
address = '2059 W 87th St. Inglewood CA. 92049.'
time = '8:00 pm'

intro = 'Dear '
message = 'You have been formally invited to a dinner at ' + address + ' Starting at ' + time
guest_qty = len(guest_list)

print(intro + guest_list[0].title() + ',\n' + message + '\n')

print(intro + guest_list[1].title() + ',\n' + message + '\n')

print(intro + guest_list[2].title() + ',\n' + message + '\n')

print("You are currently inviting", guest_qty, "guest to this event.")