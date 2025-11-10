###############################################################################
#   Damani Holland
#   11/09/2025
#   CS Python
###############################################################################

'''

4-12. More Loops: All versions of foods.py in this section have avoided using 
for loops when printing to save space . Choose a version of foods.py, and 
write two for loops to print each list of foods.

'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friends favorite foods are:")
for food in friends_food:
    print(food)

my_foods.append('cannoli')
friends_food.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)


print("\nMy friends favorite foods are:")
for food in friends_food:
    print(food)