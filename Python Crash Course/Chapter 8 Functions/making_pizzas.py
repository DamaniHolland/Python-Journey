###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################

# Importing an Entire Module
import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing Specific Functions
from pizza_module import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using 'as' to Give a Function an Alias

'''
Syntax:
    - from module_name import function_name as fn
'''
from pizza_module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module

'''
Syntax:
    - from module_name import *
'''

from pizza_module import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

