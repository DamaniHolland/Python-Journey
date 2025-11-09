###############################################################################
#   Damani Holland
#   6/23/2025
#   CS Python
###############################################################################

# 3-6 More Guest

'''
    You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.

• Use insert() to add one new guest to the beginning of your list.

• Use insert() to add one new guest to the middle of your list.

• Use append() to add one new guest to the end of your list.

• Print a new set of invitation messages, one for each person in your list.
'''

guest_list = ['the creator', 'donald trump', 'isaac newton']
address = '2059 W 87th St. Inglewood CA. 92049.'
time = '8:00 pm'

intro = 'Dear '
message = 'You have been formally invited to a dinner at ' + address + ' Starting at ' + time

print(intro + guest_list[0].title() + ',\n' + message + '\n')

print(intro + guest_list[1].title() + ',\n' + message + '\n')

print(intro + guest_list[2].title() + ',\n' + message + '\n')

print('It turns out i have a larger table available.\n')

guest_list.insert(0, 'obama')
guest_list.insert(2, 'amiri')
guest_list.append('neil degrasse tyson')

print(intro + guest_list[0].title() + ',\n' + message + '\n')

print(intro + guest_list[1].title() + ',\n' + message + '\n')

print(intro + guest_list[2].title() + ',\n' + message + '\n')

print(intro + guest_list[3].title() + ',\n' + message + '\n')

print(intro + guest_list[4].title() + ',\n' + message + '\n')

