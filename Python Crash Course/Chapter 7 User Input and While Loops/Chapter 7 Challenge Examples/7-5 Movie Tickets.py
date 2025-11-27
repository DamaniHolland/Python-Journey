###############################################################################
#   Damani Holland
#   11/27/2025
#   CS Python
###############################################################################

'''

7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
a person’s age . If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15 . Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket

'''
instructions = 'Please enter the amount of people you wish to recieve tickets ' \
                'for: '
guest_size = int(input(instructions))

amount = 0
guest_ticket_cost = []
while amount < guest_size:
    instructions = 'Please enter your age: '
    user_age = int(input(instructions))
    if user_age < 3:
        ticket_price = 0
    elif user_age >= 3 and user_age < 12:
        ticket_price = 10
    else:
        ticket_price = 15
    guest_ticket_cost.append(ticket_price)
    amount += 1
print("\nThe sum of all the tickets is: " + "$" + str(float(sum(guest_ticket_cost))))