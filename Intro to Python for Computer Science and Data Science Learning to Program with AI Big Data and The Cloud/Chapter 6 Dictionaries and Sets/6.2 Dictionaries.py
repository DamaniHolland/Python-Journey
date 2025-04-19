###############################################################################
#   Damani Holland
#   4/12/2025
#   CS Python 121
###############################################################################

# 6.2.1 Creating a Dictionary

'''
Dictionary Syntax:

   dictionary = {'key': 'value'}
'''

# 6.2 Exercise 3

states = {'California': 'CA', 'Nevada':'NV', 'Texas':'TX'}

print(states)

# 6.2.2 Iterating through a dicionay

'''
iteration syntax:

    for 'key', 'value' in dictionary_var.items():
        expression
'''
days_per_month = {'January': 31, 'February': 28, 'March': 31}

print(days_per_month)

for month, days in days_per_month.items():
    print(f'{month} has {days} days')
    
# 6.2.3 Basic Dictionary Operations

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

print(roman_numerals)

'''
Accessing The Value Associated with a Key

    - dictionary['key']
        [out]: 'Value'
'''

print(roman_numerals['X'])

'''
Updating the Value of an Eisting Key-Value Pair

    - dictionary['existing_key'] = new 'value'
'''

roman_numerals['X'] = 10

print(roman_numerals)

'''
Adding a New Key-Value Pair

    - dictionary_var['new key'] = 'new value'
'''

roman_numerals['L'] = 50

print(roman_numerals)

'''
Removing a Key-Value Pair
-You can delete a key-value pair from a dictionary with del statement
    - del dictionary_var['existing_key']

- You can remove a key-value pair with the dictionary method '.pop()'
   Which returns the value for the removed key:
    - dictionary_var.pop('existing_key')
'''

del roman_numerals['III']

print(roman_numerals)

print(roman_numerals.pop('X'))

'''
Attempting to Access a Nonexistent Key

    -dictionary_var.get('nonexistent_key', 'message if not found')
'''

print(roman_numerals.get('III', 'III not in dictionary'))

print(roman_numerals['V'])

'''
Testing whether a Dictionary Contains a specified Key

    - 'key' in dictionary_var
'''

print('V' in roman_numerals)

print('III' in roman_numerals)

print('III' not in roman_numerals)

# 6.2 Exercise 3

'''
String dictionary keys are case sensitive. Confirm this by using the
following dictionary and assigning 10 to the key 'x'—doing so adds a new key–value pair
rather than correcting the value for the key 'X':
'''
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

print(roman_numerals)
roman_numerals['x'] = 10
print(roman_numerals)

# 6.2.4 Dictionary Methods keys and values

months = {'January': 1, 'February': 2, 'March': 3}

'''
Iterating through keys and values

To iterate through keys use '.keys()'
    - for key_var in dictionary.keys():
        expression  

To iterate through values use '.values()'
    - for value_var in dictionary.vaue():
        expression
'''

for month_name in months.keys():
    print(month_name, end='    ')
    
for month_number in months.values():
    print(month_number, end='   ')
    
# Dictionary Views

'''
Dictionary methods items, keys and values each return a view of a dictrionary's
data. meaning even if you assign the method .keys() to a variable it doesn't 
create a new copy. It instead let's you view the orginal data set

'''

months_view = months.keys() # assigns keys pulled from months to months_view as a view

for key in months_view: # iterate through view of months keys
    print(key, end='    ')
    
months['December'] = 12 # updates original dictionary with new key-value pair

print(months)

for key in months_view: # variable assigned to months keys is updated as well
    print(key, end='    ')
    
# Converting Dictionary Keys, Values and Key-Value Pairs to Lists

'''
list(dictionary.key_values())
returns a view of key values from dictionary months
'''
print('\n', list(months.keys()))

print('\n', list(months.values()))

print('\n', list(months.items()))

# Processing Keys in Sorted Order

for month_name in sorted(months.keys()):
    print(month_name, end='   ')
    
# 6.2.4 Exercise 3

'''
For the following dictionary, create lists of its keys, values and items
and show those lists.
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}
'''

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}

print(list(roman_numerals.keys()))

print('\n')

print(list(roman_numerals.values()))

print('\n')

print(list(roman_numerals.items()))

# 6.2.5 Dictionary Comparisons

'''
The comparisons operators == and != can be used to determine whether two 
dictionaries have identical or different contens.
'''

country_capitals1 = {'Belgium': 'Brussels', 'Haiti': 'Port-au-Prince'}

country_capitals2 = {'Nepal': 'Kathamandu', 'Uruguay': 'Montevideo'}

country_capitals3 = {'Haiti': 'Port-au-Prince', 'Belgium': 'Brussels'}

print(country_capitals1 == country_capitals2)

print(country_capitals1 == country_capitals3)

print(country_capitals1 != country_capitals2)

# 6.2.6 Example: Dictionary of Student Grades

'''
The script below represents an instructor's grade book as a dictionary that 
maps each student's name (a string) to a list of integers containing that 
student's grades on three exams.
'''

# Usng a dictionary to represent an instructor's grade book
grade_book = {
    'Susan': [92, 85, 100],
    'Eduardo': [83, 95, 79],
    'Azizi': [91, 89, 82],
    'Pantia': [97, 91, 92]
}

# Creating a total and count to accumulate
all_grades_total = 0
all_grades_count = 0

# for each iteration unpack dictionary to variables 'name' for keys and 'grades' for values
for name, grades in grade_book.items():
    
    # accumulates integers in grades for find total sum and assign it to variable 'total'
    total = sum(grades)
    
    # Print format to display name and average grade for single person
    print(f'Averages for {name} is {total/len(grades):.2f}')
    
    # accumulates total and adds it to global total
    all_grades_total += total
    
    # accumulates length of grades and adds to global count of grades
    all_grades_count += len(grades)

# print format average for whole class    
print(f"Class's Average is: {all_grades_total / all_grades_count:.2f}")

# 6.2.7 Example: Word Counts^2

'''Tokenizing a string and counting unique words.'''

text = ('this is a sample text with several words '
        'this is more sample text with some different words')

word_counts = {} # where we store unique words and their counts

# count occurrences of each unique word
'''
line 272 tokenizes the string by calling it into the split method
'''
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1 # update existing key-value pair
    else:
        word_counts[word] = 1 # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
    
print('\nNumber of unique words:', len(word_counts))

# Python Standard Library Module collections

'''
The module collections contains the type 'Counter', which recieves
an iterable and summarizes its elements
'''

from collections import Counter

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
    
print('Number of unique keys:', len((counter.keys())))

# 6.2.7 Exercise 2

'''
Use a comprehension to create a list of 50 random integers in the
range 1–5. Summarize them with a Counter. Display the results in two-column format.
'''
import random

list = list([random.randrange(1, 6) for i in range(50)])

print(list)

numbers_counter = Counter(list)

for number, count in sorted(numbers_counter.items()):
    print(f'{number:<4}{count}')

# 6.2.8 dictionary Method .update()

'''
.update() allows you to insert and update key-value pairs using inside a
dictionary
'''
country_codes = {} # Creates and empty dictionary

print('empty dictionary: country_codes =', country_codes)

country_codes.update({'South Africa': 'za'}) # inserts into empty dictionary

print('updated dictionary: country_codes =', country_codes)

country_codes.update(Australia='ar') # inserts at the end of dictionary

print('updated dictionary: country_codes =', country_codes )

country_codes.update(Australia='au') # updates the value for 'Australia key

print('revised dictionary: country_codes =', country_codes)

# 6.2.9 Dictionary Comprehensions

months = {'January': 1, 'February': 2, 'March': 3} # Creates a dictionary containing months

'''
Remove '#' to see different result
'''
# months = {'January': 1, 'February': 2, 'March': 2} 
months2 = {number: name for name, number in months.items()} # Creates a dictionary comprehension with conditions

print(months2)

'''
The expression 'number: name' specifies a key-value pair of the form 'key: value'
'in months.items()' iterates through dictionary months, unpacking each key-value pair
tuple into variables 'name' and 'number' using expression 'for name, number'
The expression 'number: name' reverses the key and value, so the new dictionary
maps the months numbers to the months names and the months names to the months
numbers. Having duplicate values in the original dictionary causes the comprehension
to update the key: value by inserting the new value to the existing key.
'''
grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}
print(grades)
'''
dictionary comprehension syntax:

var = {new_key: new_value, for key_var, value_var in dictionary.items()}
'''
grades2 = {student: sum(grades) / len(grades) for student, grades in grades.items()}
print(grades2)

# Self Check 6.2.9 exercise 1

'''
Use a dictionary comprehension to create a dictionary
of the numbers 1–5 mapped to their cubes:
'''
cubes = {num: num**3 for num in range(1, 6)}
print(cubes)