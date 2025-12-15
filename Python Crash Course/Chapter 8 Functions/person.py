###############################################################################
#   Damani Holland
#   12/13/2025
#   CS Python
###############################################################################

# Returning a Dictionary

    # creat function 'build_person' that take 2 arguments 'first_name', 
        #'last_name
        # create variable 'person' and assign it to dictionary key - value pair
            # 'first': first_name, 'last': last_name
        # returns the values stored in person
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

    # create variable 'musician' and assign it to function 'build_person'
        # with arguments 'jimi', 'hendrix'
    # display dictionary of information stared in 'musician'
musician = build_person('jimi', 'hendrix')
print(musician)

    # create function 'build_persion' that takes 3 arguments 'first_name',
        # 'last_name', and 'age' and set age as an optional parameter 
        # assigning an empty string value
        
        # create variable 'person' and assign it to key-value pairs 
        # 'first': first_name, 'last: last_name
        # age is modified from default value in any way:
            # dictionary 'person' adds a new key ['age'] assigned to value 'age'
        
        # return dictionary information in variable 'person'
        
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

    # variable 'musician' assigned to function 'build_person' with arguments
        # 'jimi', 'hendrix', 'age=27'
    # display 'musician'
musician = build_person('jimi', 'hendix', age=27)
print(musician)

# Using a Function with a while loop

    # create function 'get_formatted_name' with 2 arguments 'first_name', 
    # 'last_name'
        # variable 'full_name' is assigned to 'first_name' + 'last_name'
        # return variable 'full_name' with '.title()' method
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

    # This is an infinite loop!
    
    # initiate while loop with active value 'True'
        # display instructions
        
        # variable 'f_name' is assigned to user input value
        # if 'f_name' is 'q'
            # stop loop
            
        # variable 'l_name' is assigned to user input value
        # if 'l_name' is 'q'
            # stop loop
            
        # variable 'formatted_name' is assigned to function get_formatted_name
        # with two arguments 'f_name', l_name'
        
    # display string with formatted_name
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last_name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    
