###############################################################################
#   Damani Holland
#   11/09/2025
#   CS Python
###############################################################################

'''

4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 60) . Make a copy of the list of pizzas, and call it friend_pizzas . 
Then, do the following:

•  Add a new pizza to the original list .

•  Add a different pizza to the list friend_pizzas .

•  Prove that you have two separate lists . Print the message, My favorite 
pizzas are:, and then use a for loop to print the first list . Print the message, 
My friend’s favorite pizzas are:, and then use a for loop to print the sec-
ond list . Make sure each new pizza is stored in the appropriate list

'''

pizzas = ["pepperoni", "hawaiian", "meat lovers"]
for pizza in pizzas:
    print("large " + pizza + " pizza")
    
print("Pizza is my favorite food")

friend_pizzas = pizzas[:]

pizzas.append('veggie')

friend_pizzas.append('supreme')

print("\nMy favortie pizzas are:")
for pizza in pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)