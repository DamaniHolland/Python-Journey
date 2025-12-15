###############################################################################
#   Damani Holland
#   12/08/2025
#   CS Python
###############################################################################

# Return Values

'''

Return Value:

    - The value the function returns
    
'''

    # create a function with arguments 'first_name', 'last_name')
        # create variable 'full_name' and assign arguments 'first_name, 
            # 'last_name'
        # function returns value stored in variable 'full_name' with 
            # '.title()' method
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

    # create variable 'musician' and assign it to function 'get_formatted_name'
        # with arguments 'jimi', 'hendrix'
    # display formatted name 'Jimi Hendrix'
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

    # Making and Argument Optional

    # create function 'get_formatted_name' with arguments 'first_name',
        # 'last_name', 'middle_name', 'last_name'
        
        # create variable 'full_name' and assign it to 'first_name', 
            # 'middle_name' and 'last_name'
        # return value stored in 'full_name' with '.title()' method
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

    # create variable 'musician' and assign it to function 'get_formatted_name'
        # with arguments 'john', 'lee', 'hooker'
    # display formatted name 'John Lee Hooker'
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


    # create function 'get_formatted_name' with arguments 'first_name', 
        # 'last_name', 'middle_name'
        
        # if middle_name has been filled in with any string value
            # create variable 'full_name' with arguments 'first_name', 
            # 'middle_name', 'last_name'
        # else middle name has not been filled in
            # create variable 'full_name' and assign  it to 'first_name' 
            # 'last_name'
            
        # return variable 'full_name' with '.title()' method
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

    # create a variable 'musician' and assign it to function 
        # 'get_formatted_name with arguments 'jimi', and 'hendrix'
    # display formatted name 'Jimi Hendrix'
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

    # Create variable 'musician' and assign it to function 'get_formatted_name'
        # with arguments 'john', 'hooker', and 'lee'
    # display formatted name 'John Lee Hooker'
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

