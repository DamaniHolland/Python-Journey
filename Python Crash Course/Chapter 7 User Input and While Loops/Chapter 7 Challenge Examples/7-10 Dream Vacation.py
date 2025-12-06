###############################################################################
#   Damani Holland
#   12/02/2025
#   CS Python
###############################################################################

'''

7-10. Dream Vacation: Write a program that polls users about their dream 
vacation . Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll

'''

dream_vacation = {}

polling_active = True

while polling_active:
    vacation_destination = input("If you could go on a dream vacation, where would it be? ")
    name = input("What is your name? ")
    dream_vacation[name] = vacation_destination
    
    repeat_poll =  input("Would you like to enter another dream vacation destination? ")
    
    if repeat_poll == 'no':
        polling_active = False

print("\n--- Poll Results ---")
        
for name, vacation_destination in dream_vacation.items():
    print(name.title() + " would like to got to " + vacation_destination.title() + ".")