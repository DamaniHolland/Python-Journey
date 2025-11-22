###############################################################################
#   Damani Holland
#   11/21/2025
#   CS Python
###############################################################################

'''
6-5. Rivers: Make a dictionary containing three major rivers and the country 
each river runs through . One key-value pair might be 'nile': 'egypt' .

•  Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt .

•  Use a loop to print the name of each river included in the dictionary .

•  Use a loop to print the name of each country included in the dictionary

'''
'''
mississippi = {'name': 'mississippi river', 'location': 'mississippi', 
            'length': '3,902 miles'
            }
nile = {'name': 'nile river', 'location': 'egypt, sudan', 
        'length': '4,135 miles'
        }
amazon = {'name': 'amazon river', 
          'location': 'brazil, venezuela, bolivia, and ecuador', 
          'length': '3,980 miles'
          }
ob = {'name': 'ob, irtysh', 'location': 'russia, china, mongolia', 
      'length': '3,364 miles'}
yangtze = {'name': 'yangtze river', 'location': 'china', 
           'length': '3,917 miles'}

rivers = [mississippi, nile, amazon, ob, yangtze]

for river in rivers:
    print(river['name'].title() + ' located in ' + river['location'].title() + ".")
    print('name: ' + river['name'].title())
    print('location: ' + river['location'].title())
 '''   


rivers = {
    'mississippi': 'mississippi', 
    'egypt': 'nile',
    'china': 'Yangtze', 
    'russia': 'lena', 
    'china': 'yellow'    
    }

for location, name in rivers.items():
    print("The " + name.title() + " River is located in " + 
          location.title() + ".")
    
for name in rivers.values():
    print('name: ' + name.title() + " River")
    
for location in rivers.keys():
    print('location: ' + location.title())