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

def build_person(first, last):
    person = {}
    
    person['first_name'] = first
    person['last_name'] = last
    
    return person

def formatted_name(person_name):
    first_name = person_name['first_name']
    last_name = person_name['last_name']
    
    full_name = first_name.title() + " " + last_name.title()
    
    return full_name
        