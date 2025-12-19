###############################################################################
#   Damani Holland
#   12/18/2025
#   CS Python
###############################################################################

# Creating and Using a Class
        
class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# Making an Instance from a Class

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

    # Accessing Attributes
    
'''

Syntax:

    - class_varialbe.attribute

'''

    # Calling Methods
'''

Syntax:

    - class_variable.method

'''
my_dog.sit()
my_dog.roll_over()

    # Creating Multiple Instances
    
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + ' years old.')
your_dog.sit()
