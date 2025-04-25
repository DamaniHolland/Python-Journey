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

'''
Adding Elements to a list

Syntax: 
    - list_name.append('new_value')   
'''

motorcycles.append('ducati')
print('modified list:', motorcycles)