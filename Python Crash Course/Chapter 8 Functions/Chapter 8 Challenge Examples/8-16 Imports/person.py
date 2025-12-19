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
user = person_module.build_person('damani', 'holland')
full_name = person_module.formatted_name(user)
print(full_name)

from person_module import build_person
from person_module import formatted_name
user = build_person('damani', 'holland')
full_name = formatted_name(user)
print(full_name)

from person_module import build_person as bp
from person_module import formatted_name as fn
user = bp('damani', 'holland')
full_name = fn(user)
print(full_name)

import person_module as pm
user = pm.build_person('damani', 'holland')
full_name = pm.formatted_name(user)
print(full_name)

from person_module import *
user = build_person('damani', 'holland')
full_name = formatted_name (user)
print(full_name)