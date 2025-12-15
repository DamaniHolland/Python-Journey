###############################################################################
#   Damani Holland
#   12/13/2025
#   CS Python
###############################################################################


'''

8-6. City Names: Write a function called city_country() that takes in the name 
of a city and its country . The function should return a string formatted like this:

"Santiago, Chile"

'''

def city_country(city_name, country):
    print(city_name.title() + ", " + country.title())
    
city_country('tokyo', 'japan')
city_country('paris', 'france')
city_country('los angeles', 'united states of america')