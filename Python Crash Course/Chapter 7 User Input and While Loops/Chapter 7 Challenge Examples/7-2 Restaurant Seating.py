###############################################################################
#   Damani Holland
#   11/26/2025
#   CS Python
###############################################################################

'''

7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group . If the answer is more than eight, print a message say-
ing they’ll have to wait for a table . Otherwise, report that their table is ready.

'''

num_of_guest = input("How many guest for tonight's reservation? ")
num_of_guest = int(num_of_guest)

if num_of_guest > 8:
    print("I do apologize, but you will have to wait for a table.")
else:
    print("Perfect, I will have a table ready for " + str(num_of_guest) + ".")