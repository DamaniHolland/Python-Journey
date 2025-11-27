###############################################################################
#   Damani Holland
#   11/26/2025
#   CS Python
###############################################################################

# Introducing While Loops


'''
while Loops

    - The while loop runs as long as, or 'while', a certain condition is true.
'''
    # The While Loop in Action

    # assign value '1' to 'current_number'
current_number = 1

    # while 'current_number' is less than or equal to '5'
        # print 'current_number'
        # add 1 to 'current_number' and assign new value to 'current_number'
while current_number <= 5:
    print(current_number)
    current_number += 1
    
# Using Continue in a Loop

'''
continue Statement:

    - The continue statement to return to the beginning of the loop based on 
      the result of a conditional test.
'''

    # Assign value '0' to variable 'current_number'
current_number = 0

    # While variable 'current_number' is less than 10
        # Add 1 to the current value stored inside current_number
        # If current_number divided by two returns a remainder of 0
            # return to beginning of the loop
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    # print value inside 'current_number'
    print( current_number)
    
# Avoiding Infinite Loops

x = 1
print('\nCounting to 5: ')

    # while variable 'x' is less than or equal tp 5
        # Print variable (x)
        # variable (x) add 1 and assign new value to variable (x).
while x <= 5:
    print(x)
    x += 1 # <----remove this to create an infinite loop'
    # If stuck in infinite loop press 'CTRL + C' to close the terminal.