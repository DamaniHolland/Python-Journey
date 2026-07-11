###############################################################################
#   Damani Holland
#   7/10/2026
#   CS Python
###############################################################################

file_name = 'Python Crash Course\Chapter 10 Files and Exceptions\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
"""
We create a variable, pi_string to hold the digits of pi.
"""

for line in lines:
    """
    Use 'for' loop that adds each line of digits to pi_string and removes 
    the newline character from each line.
    """
    
    pi_string += line.strip()
    """
    The variable pi_string contains the whitespace that was on the left side 
    of the digits in each line, but we can get rid of that by using strip() instead 
    of rstrip():
    """
    
print(pi_string)
print(len(pi_string))
"""
We print this string and show how long the string is.
"""
