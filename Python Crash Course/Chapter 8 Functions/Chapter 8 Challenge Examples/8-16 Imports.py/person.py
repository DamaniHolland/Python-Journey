###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################

'''
8-16. Imports: Using a program you wrote that has one function in it, store that 
function in a separate file . Import the function into your main program file, and 
call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

'''

import person_module

user = person_module.build_person('damani', 'hollland')