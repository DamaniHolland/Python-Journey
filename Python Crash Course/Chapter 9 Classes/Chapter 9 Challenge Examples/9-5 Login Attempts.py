###############################################################################
#   Damani Holland
#   7/5/2026
#   CS Python
###############################################################################
"""
9-5. Login Attempts: Add an attribute called login_attempts to your User 
class from Exercise 9-3 (page 166) . Write a method called increment_
login_attempts() that increments the value of login_attempts by 1 . Write 
another method called reset_login_attempts() that resets the value of login_
attempts to 0 .Make an instance of the User class and call increment_login_attempts() 
several times . Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts() . Print login_attempts again to 
make sure it was reset to 0.
"""

"""
9-3. Users: Make a class called User . Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile . Make a method called describe_user() that prints a summary 
of the user’s information . Make another method called greet_user() that prints 
a personalized greeting to the user .Create several instances representing different 
users, and call both methods for each user .
"""

'''
9-5 Completed :P
'''

class User():
    
    # Methods
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0
    def describe_user(self):
        print("\nUser Information:")
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(str(self.login_attempts))
    
    def greet_user(self):
        print("\nHello! " + "Welcome " + self.first_name)

    def increment_login_attempts(self):        
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts
# Calling methods
        
user_One = User('damani', 'holland', 'damanirayholland@gmail.com')

user_One.describe_user()
user_One.greet_user()

user_Two = User('amiri', 'aje', 'amiriaje@yahoo.com')

user_Two.describe_user()
user_Two.greet_user()

user_Three = User('dawnly', 'sielle', 's.dawnly@gmail.com')

user_Three.describe_user()
user_Three.greet_user()

user_One.increment_login_attempts()
user_One.increment_login_attempts()
user_One.increment_login_attempts()
user_One.increment_login_attempts()
user_One.describe_user()

user_One.reset_login_attempts()
user_One.describe_user()