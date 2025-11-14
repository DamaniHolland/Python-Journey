###############################################################################
#   Damani Holland
#   11/14/2025
#   CS Python
###############################################################################

# The if-elif-else Chain

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission is $5.")
else:
    print("Your admission cost is $10")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("\nYour admission cost is $" + str(price) + ".")

# Using Multiple elif Blocks

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("\nYour admission cost is $" + str(price) + ".")
