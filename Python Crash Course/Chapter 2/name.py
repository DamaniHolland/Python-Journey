###############################################################################
#   Damani Holland
#   4/24/2025
#   CS Python 121
###############################################################################

# Changing Case in a String With Methods

name = "ada lovelace"

'''
The '.title()' method displays each word in titlecase, where each word begins
with a capital letter.
'''
print('original:', name)
print('.title() method:', name.title()) 

name = 'Ada Lovelace'
print('Original:', name)
print('.upper() method:', name.upper())
print('.lower() method', name.lower())

# Combining or Concatenating Strings


'''
This is an example of cancatenation using the '+' to assign variables 'fisrt_name'
'last_name' and ' ' to variable 'full_name'
'''
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

'''
We can use concatenation to compose a message and then store the entire message
in a variable
'''
message = "Hello, " + full_name.title() + "!"

print(message)