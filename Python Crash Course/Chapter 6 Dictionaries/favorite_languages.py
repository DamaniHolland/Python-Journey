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