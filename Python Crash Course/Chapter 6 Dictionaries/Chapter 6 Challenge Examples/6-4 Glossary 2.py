###############################################################################
#   Damani Holland
#   11/21/2025
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

glossary = {
    'lists': '"A lists is a collection of items in a particular order. The '
            'list can include letters of the alphabet and/or digits 0-9."', 
    'variable': '"Variables are containers for storing data values."', 
    'strings': '"A sequence of characters, representing text."', 
    'for loop': '" A control statement used for iteration, allowing a block '
                'of code to be executed repeatedly in a sequence or other '
                'iterable object."', 
    'index': '"Refers to the numerical position of an element within a '
            'sequence, such as a list, string, or tuple."', 
    'if': '"Used to create conditional execution, allowing specific blocks '
            'of code to run only when a given condition evaluates to True."', 
    '.sort()': '"A common function for arranging elements within a data '
                'structure, typically an array or list, into a specific order."', 
    'dictionary': '"An unordered collection of dara values, used to store data '
                    'in key:value pairs."', 
    '.items()': '"When called on a dictionary, returns a view object that displays '
                'a list of key-value tuple pairs."', 
    '.lower()': '"Used to convert all lowercase equivalents. It returns a new '
                'string unchaged because strings are immutable."'
    
    }


for term in glossary:
    print(term + ": "  + glossary[term])
    print("\n") 