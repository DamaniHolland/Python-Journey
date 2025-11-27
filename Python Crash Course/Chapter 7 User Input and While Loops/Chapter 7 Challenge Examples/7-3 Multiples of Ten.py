###############################################################################
#   Damani Holland
#   11/26/2025
#   CS Python
###############################################################################

'''

7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not .

'''

user_num = input("Please enter a number: ")

user_num = int(user_num)

if user_num % 10 == 0:
    print("\nThe number " + str(user_num) + " is a multiple of ten.")
else:
    print("\nThe number " + str(user_num) + " is not a multiple of ten.")