###############################################################################
#   Damani Holland
#   11/25/2025
#   CS Python
###############################################################################


'''

6-11. Cities: Make a dictionary called cities . Use the names of three cities as 
keys in your dictionary . Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city . The keys for each city’s dictionary should be something like 
country, population, and fact . Print the name of each city and all of the infor-
mation you have stored about it

'''

cities = {'los angeles': {'city_name': 'los angeles', 
                         'country_located': 'united states of america',
                         'total_area_(sq_miles)': 502.7},
         'san diego': {'city_name': 'san diego', 
                       'country_located': 'united states of america',
                       'total_area_(sq_miles)': 372.4},
         'san francisco': {'city_name': 'san francisco', 
                           'country located': 'united states of america',
                           'total_area_(sq_miles)': 231.89}
        }

for city, information in cities.items():
    print("\nName: " + city.title())
    for info_title, data in information.items():
        if info_title == 'total_area_(sq_miles)':
            print("\t" + info_title + ": " + str(data) + ' sq. miles')
        else:
            print("\t" + info_title + ": " + str(data).title())
        