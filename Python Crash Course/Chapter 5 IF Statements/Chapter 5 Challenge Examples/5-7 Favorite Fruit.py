###############################################################################
#   Damani Holland
#   11/16/2025
#   CS Python
###############################################################################

'''

5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
independent if statements that check for certain fruits in your list .

•  Make a list of your three favorite fruits and call it favorite_fruits .

•  Write five if statements . Each should check whether a certain kind of fruit 
is in your list . If the fruit is in your list, the if block should print a statement, 
such as You really like bananas!

'''

favorite_fruits = ['apples', 'bananas', 'oranges']

if 'grapes' not in favorite_fruits:
    print("I also don't like grapes.")

if 'apples' in favorite_fruits:
    print("Apple a day keep the doctor away")

if 'oranges' in favorite_fruits:
    print("Navel or Cara Cara?")
    
if 'bananas' in favorite_fruits:
    print("You really like bananas!")