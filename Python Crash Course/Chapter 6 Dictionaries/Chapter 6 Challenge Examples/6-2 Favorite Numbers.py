###############################################################################
#   Damani Holland
#   11/18/2025
#   CS Python
###############################################################################

'''

6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers . 
Think of five names, and use them as keys in your dictionary . Think of a favorite 
number for each person, and store each as a value in your dictionary . Print 
each person’s name and their favorite number . For even more fun, poll a few 
friends and get some actual data for your program

'''

favorite_numbers = {'john': 3,
                    'dan': 7, 
                    'sam': 5,
                    'kayla': 9, 
                    'caleb': 2
                    }
less_than_five = []
greater_than_five = []
total_numbers = len(favorite_numbers)
print(total_numbers)
for favorite_number in favorite_numbers:
    print(favorite_number + 
          ": " + 
          str(favorite_numbers[favorite_number]))
    if favorite_numbers[favorite_number] <= 5:
        less_than_five.append(str(favorite_number))
    else:
        greater_than_five.append(str(favorite_number))

if less_than_five > greater_than_five:
    print('People prefer a number smaller than 5.')
else:
    print('People prefer a number greater than five.')
print('people who prefer a number less than five: ' + str(less_than_five))
print('people who prefer a number greater than five: ' + str(greater_than_five))