###############################################################################
#   Damani Holland
#   12/01/2025
#   CS Python
###############################################################################

# Romoving all Instances of specific Values from a list

'''

remove() Function:

    - used to remove a specific value from a list
    
'''

    # assign list of pets to variable pets
    # print list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

    # while string 'cat' in list 'pets'
        # remove value 'cat' from list
while 'cat' in pets:
    pets.remove('cat')
    
    # print list
print(pets)
