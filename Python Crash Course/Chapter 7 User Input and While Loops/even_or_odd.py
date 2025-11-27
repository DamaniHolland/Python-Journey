###############################################################################
#   Damani Holland
#   11/26/2025
#   CS Python
###############################################################################


    # ask user to input a number
number = input("Enter a number, and I'll tell you if it's even or odd: ")

    # changes user input type from string to integer and assigns it to number
number = int(number)

    # if number divided by 2 returns a remainder of 0
        # print this number is  even
    # else number divided by 2 returns any number that is not zero
        # print this number is odd
if number % 2 == 0:
    print("\n The number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")