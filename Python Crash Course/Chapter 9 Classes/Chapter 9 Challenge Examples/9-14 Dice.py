###############################################################################
#   Damani Holland
#   7/9/2026
#   CS Python
###############################################################################

"""
9-14. Dice: The module random contains functions that generate random num-
bers in a variety of ways . The function randint() returns an integer in the 
range you provide . The following code returns a number between 1 and 6:
from random import randint

x = randint(1, 6)

Make a class Die with one attribute called sides, which has a default 
value of 6 . Write a method called roll_die() that prints a random number 
between 1 and the number of sides the die has . Make a 6-sided die and roll 
it 10 times .Make a 10-sided die and a 20-sided die . Roll each die 10 times
"""

from random import randint



class Die():
    """Meant to represent Die and how many rolls."""
    
    def __init__(self, sides = 6):
        """Initializes the die"""
        self.sides = sides
    
    def roll_die(self, number_of_rolls):
        """shows results of rolls"""
        self.number_of_rolls = number_of_rolls
        
        message = 'Roll results for ' + str(self.sides) + ' sided die'
        message += ' for ' + str(self.number_of_rolls) + ' rolls:'
        print(message)
        
        for index in range(self.number_of_rolls):
            x = randint(1, self.sides)

            print(str(x))
        

die_One = Die()
die_One.roll_die(10)
    
die_Two = Die(10)
die_Two.roll_die(10)

die_Three = Die (20)
die_Three.roll_die(10)