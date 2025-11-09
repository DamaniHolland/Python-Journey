###############################################################################
#   Damani Holland
#   6/23/2025
#   CS Python
###############################################################################
 
# 3-7 Shrinking Guest List

'''
You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.

• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.

• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.

• Print a message to each of the two people still on your list, letting them
know they’re still invited.

• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
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

print('Dear Guest, \nI regret to inform you my new dining room table won\'t arrive in time. So i can only invite two of you can come.\nMy sincerest apologies.\n')

print(intro + guest_list.pop().title() + ',\n' + 'I regret to inform you of your uninvite to the dinner. My sincerest apologies.\n')

print(intro + guest_list.pop().title() + ',\n' + 'I regret to inform you of your uninvite to the dinner. My sincerest apologies.\n')

print(intro + guest_list.pop().title() + ',\n' + 'I regret to inform you of your uninvite to the dinner. My sincerest apologies.\n')

print(intro + guest_list.pop().title() + ',\n' + 'I regret to inform you of your uninvite to the dinner. My sincerest apologies.\n')

print(intro + guest_list[0].title() + ',\n' + message + '\n')

print(intro + guest_list[1].title() + ',\n' + message + '\n')

print(guest_list)

del guest_list[0]
del guest_list[0]

print(guest_list)