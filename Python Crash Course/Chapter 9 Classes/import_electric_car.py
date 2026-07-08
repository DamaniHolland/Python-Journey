###############################################################################
#   Damani Holland
#   7/7/2026
#   CS Python
###############################################################################

from car import ElectricCar

my_tesla  = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()