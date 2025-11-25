###############################################################################
#   Damani Holland
#   11/22/2025
#   CS Python
###############################################################################


'''

6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet . In each dictionary, include the kind of animal and the owner’s 
name . Store these dictionaries in a list called pets . Next, loop through your list 
and as you do print everything you know about each pet

'''

pets = {
    'kujo': {'pet_name': 'kujo', 
             'pet_type': 'dog', 
             'owners_name': 'rodney'
    }, 
    'kaleb': {'pet_name': 'kaleb',
              'pet_type': 'cat',
              'owners_name': 'caleb'
    },
    'king pin': {'pet_name': 'king pin',
              'pet_type': 'gold fish',
              'owners_name': 'henry'
    },
    'mondo': {'pet_name': 'monda',
              'pet_type': 'guinea pig',
              'owners_name': 'miguel'
    },
    'hector': {'pet_name': 'hector',
              'pet_type': 'tortoise',
              'owners_name': 'yuki'
    },
    'luna': {'pet_name': 'luna',
              'pet_type': 'dog',
              'owners_name': 'jasmine'
    },
}

for pet_name, info in pets.items():
    print(pet_name + ': ' + str(info).title())