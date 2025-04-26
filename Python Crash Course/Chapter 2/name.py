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

# Adding Whitespace to Strings with Tabs or Newlines

# '\t' to add tab to your text

print("\tPython")

# '\n' To add a newline in a string

print("Languages:\nPython\nC\nJavascript")

'''
You can also combine tabs and newlines in a single string. The string (\)n(\)t
tells python to move to a new line, and start the next line with a tab.
'''

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitspcae

favorite_language = "python "
punctuation = '!'
print('With Whitespace: ' + favorite_language + punctuation)
print('Without Whitespace: ' + favorite_language.rstrip() + punctuation)


favorite_language = ' python '
print('original:' + favorite_language + 'is my favorite language')
print('.rstrip() method:' + favorite_language.rstrip() + 'is my favorite language')
print('.lstrip() method:' + favorite_language.lstrip() + 'is my favorite language')
print('.strp() method:' + favorite_language.strip() + 'is my favorite language')