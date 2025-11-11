###############################################################################
#   Damani Holland
#   11/10/2025
#   CS Python
###############################################################################

# If Satements

'''
If Statements

Syntax:
    - if variable == element:
          print(variable)
      else:
          print(something else)
          
- This is an example of checking for equality
- since it is case sensitive 'Car' and 'car are not considered the same

'''

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
