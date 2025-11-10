###############################################################################
#   Damani Holland
#   11/10/2025
#   CS Python
###############################################################################

# copying a list

'''
To copy a list we use a slice to indicate which part of the list we want to copy
then assign that slice to a variable to store the information.

Syntax:
    
    - variable_name = [list, items]
      new_variable = variable_name[:]
'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]



print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_food)

'''
Now we are going to add seperate items to each list
this proves that the list are independent of each other after the slice has been
created.
'''

my_foods.append('cannoli')
friends_food.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_food)