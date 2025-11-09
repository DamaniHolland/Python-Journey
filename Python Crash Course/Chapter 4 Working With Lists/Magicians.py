###############################################################################
#   Damani Holland
#   11/08/2025
#   CS Python
###############################################################################

# Looping Through Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
'''
for magician in magicians:

    - This line tell python to take the first value in the list(magicians) which is 'alice'
    and store it in the variable 'magician'
    
print(magician)

    - This line tells Python to print the value inside the variable (magician)
    
This proccess repeats until all the items in the list have gone through this process.
'''

# Doing More Work Within a for loop

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait til I see your next trick, " + magician.title() + ".\n")
'''
for magician in magicians:

    - For current value in list (magicians)

print(magician.title() + ", that was a great trick!")

    - prints the current value as a pronoun using the .title() method.
    Then adds the string element after the value to print
'''

print("Thank you, everyone. That was a great magic show!")
