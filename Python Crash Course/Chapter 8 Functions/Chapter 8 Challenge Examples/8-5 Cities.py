###############################################################################
#   Damani Holland
#   12/12/2025
#   CS Python
###############################################################################


'''

8-5. Cities: Write a function called describe_city() that accepts the name of 
a city and its country . The function should print a simple sentence, such as 
Reykjavik is in Iceland . Give the parameter for the country a default value . 
Call your function for three different cities, at least one of which is not in the 
default country

'''

def describe_city(city, country = 'United States of America'):
    print(city.title() + " is in the " + country.title() + ".")
    
describe_city('los angeles')
describe_city('san diego')
describe_city('tokyo', 'japan')

    
