###############################################################################
#   Damani Holland
#   4/25/2025
#   CS Python
###############################################################################

# Changing, Adding, and Removing Elements

'''
Modifying elements in a list

Syntax:
    - list_name[index that already exist] = new_value
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print('original list:' , motorcycles)

#   motorcycles[0] = 'ducati'
#   print('modified list:' , motorcycles)


# Adding Elements to a list  

'''
Appending Elements to the End of a list

Syntax: 
    - list_name.append(new_value) 
'''

motorcycles.append('ducati')
print('modified list:', motorcycles)

'''
Inserting Elements into a List will shift existing values in list instead of 
replacing

Syntax:
    - list_name.insert(new_value)
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print('Inserting into list:', motorcycles)


# Removing Elements from a List

'''
Removing an Item Using the del Statement

Syntax:
    - del list_name[index_of_item]
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print('original list:', motorcycles)

del motorcycles[0]
print('deleted item using index:', motorcycles)

'''
Removing an Item Using the .pop() method

Syntax:
    - list_name.pop()
    
removes the last item from the original list
is possible to assign removed value to a variable

Syntax:
    - var_name = list_name.pop()
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print('original list:', motorcycles)

popped_motorcycles = motorcycles.pop()
print('popped list:', motorcycles)
print('Value popped:', popped_motorcycles)

'''
Popping Items from any Position in a List

Syntax:
    - var_name = list_name.pop(index_to_remove)
    
removes value in list at listed index
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

