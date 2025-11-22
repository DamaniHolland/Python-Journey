###############################################################################
#   Damani Holland
#   11/21/2025
#   CS Python
###############################################################################


# Nesting

    # Create dictionary containing 'attribute': '[list of values]'
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

    # print string statement containing 'crust' attribute
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

    # for every item in dictionary['key']
        # print dictionary ['list of values']
for topping in pizza['toppings']:
    print("\t" + topping)