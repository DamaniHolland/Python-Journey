###############################################################################
#   Damani Holland
#   6/23/2025
#   CS Python
###############################################################################

# 3-5 Changing Guest

'''
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.

• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.

• Print a second set of invitation messages, one for each person who is still
in your list.
'''

guest_list = ['the creator', 'donald trump', 'isaac newton']
address = '2059 W 87th St. Inglewood CA. 92049.'
time = '8:00 pm'

intro = 'Dear '
message = 'You have been formally invited to a dinner at ' + address + ' Starting at ' + time

print(intro + guest_list[0].title() + ',\n' + message + '\n')

print(intro + guest_list[1].title() + ',\n' + message + '\n')

print(intro + guest_list[2].title() + ',\n' + message + '\n')

print('Dear attendees, \n ' + guest_list[0].title() + ' will be unavailable for the event.\n')

guest_list[0] = 'amiri'

print(intro + guest_list[0].title() + ',\n' + message + '\n')

print(intro + guest_list[1].title() + ',\n' + message + '\n')

print(intro + guest_list[2].title() + ',\n' + message + '\n')