###############################################################################
#   Damani Holland
#   7/9/2026
#   CS Python
###############################################################################

'''

6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 102) by replacing your series of print 
statements with a loop that runs through the dictionary’s keys and values . 
When you’re sure that your loop works, add five more Python terms to your 
glossary . When you run your program again, these new words and meanings 
should automatically be included in the output

'''

'''

6-3. Glossary: A Python dictionary can be used to model an actual dictionary . 
However, to avoid confusion, let’s call it a glossary .

•  Think of five programming words you’ve learned about in the previous 
chapters . Use these words as the keys in your glossary, and store their 
meanings as values .

•  Print each word and its meaning as neatly formatted output . You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line . Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output

'''

"""
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you 
used a standard dictionary to represent a glossary . Rewrite the program using 
the OrderedDict class and make sure the order of the output matches the order 
in which key-value pairs were added to the dictionary.
"""
from collections import OrderedDict

glossary = OrderedDict()




glossary['list'] = ("A lists is a collection of items in a particular order. " + 
                    "The list can include letters of the alphabet and/or digits 0-9.")

glossary['variables'] = ("Variables are containers for storing data values.")

glossary['strings'] = 'A string is a sequence of characters, representing text.'

glossary['for loop'] = ("a for loop is a control flow statement used for iteration, " + 
                        "allowing a block of code to be executed repeatedly for each " + 
                        "item in a sequence or other iterable object.")
glossary['index'] = ("an index refers to the numerical position of an element within " + 
                     "a sequence, such as a list, string, or tuple.")
glossary['exceptions'] = ("special objects Python creates to manage errors that arise " +
                          "while a program is running.")
glossary['json module'] = ("allows yyou to save user data so it isn't lost when your " + 
                           "program stops running.")
glossary['file path'] = ("Tells python to look in a specific location on your system")
glossary['relative path'] = ("Tells Python to look for a given location relative to the " +
                             "directory where the currently running program file is stored.")
glossary["absolute path"] = ("Tells Python exactly where the file is on your computer " +
                             "regardless of where the program that's being executed is stored.")
for term in glossary:
    print(term.title() + ": " + glossary[term])
    print("\n")