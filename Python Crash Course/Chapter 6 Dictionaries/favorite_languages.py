###############################################################################
#   Damani Holland
#   11/18/2025
#   CS Python
###############################################################################

    # A Dictionary of Similar Objects

favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python'
    }
    
    # Create a list[] assinged(=) to variable 'friends'
        # list contains two items 'phil' and 'sarah

friends = ['phil', 'sarah']
   
    # Created a for loop using 'for.'
    # called in two variables with 'name' and 'language.'
        # These two variables store key_value pairs from dictionary.
    # assigned for loop to dictionary named 'favorite_languages.'
    # and called '.items()' method, which returns key_values as pairs  

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
    
    # Create a 'for' loop to iterate through all items inside dictionary
        # print name with a '.title()' method
        
for name in favorite_languages.keys():
    print(name.title())
    
    # create a conditional using 'if'
            # if name is in 'favorite_laguages' and 'friends'
                # print additional satements

    if name in friends:
        print(" Hi " + name.title() +
              ", I see you favorite language is " + 
              favorite_languages[name].title() + "!")

    # Create a conditional using 'if'
    # check to see if string 'erin' is not found in keys of favorite_languages{}
    # if not found in favorite_languages than print 'string statement'

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# Looping Through a Dictionary's Keys in Order

    # Create a 'for' loop 'temp_variable' 'in' sortded(dictionary_variable.keys())(method):
        # print(temp_variable.title()(method) + "string statement")
        
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", Thank you for taking the poll!")
    
    # Print a string statement
    # Create 'for' loop to iterate through all values in dictionary
    # for every value in dictionary print temp_variable.title() method
    
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
    # When you wrap set() around a list that contains duplicate items, 
    # Python identifies unique items in the list and builds a set from those items
    # Creates a nonrepetitive list of languages that have been mentioned
    # in the poll.
    
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    
