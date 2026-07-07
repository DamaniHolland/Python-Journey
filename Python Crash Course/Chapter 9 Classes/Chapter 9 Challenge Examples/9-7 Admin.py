###############################################################################
#   Damani Holland
#   7/6/2026
#   CS Python
###############################################################################

"""
9-7. Admin: An administrator is a special kind of user . Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on . 
Write a method called show_privileges() that lists the administrator’s set of 
privileges . Create an instance of Admin, and call your method.
"""

'''
9-3. Users: Make a class called User . Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile . Make a method called describe_user() that prints a summary 
of the user’s information . Make another method called greet_user() that prints 
a personalized greeting to the user .Create several instances representing different 
users, and call both methods for each user .
'''
class User():
    
    def __init__(self, first_name, last_name, username, email,):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        
    def describe_user(self):
        message = "User Information:"
        message += "\n\tFirst Name: " + self.first_name.title()
        message += "\n\tLast Name: " + self.last_name.title()
        message += "\n\tUsername: " + self.username
        message += "\n\tEmail: " + self.email
        
        print(message)
    
    def greet_user(self):
        message = "Greetings " + self.first_name.title()
        message += "\nWelcome to the Software!"
        
        print(message)
        
class Admin(User):
    
    def __init__(self, first_name, last_name, username, email):
        super(Admin, self).__init__(first_name, last_name, username, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def describe_privileges(self):
        print("List of Privileges: ")
        for privilege in self.privileges:
            message = "\n\t" + privilege
            print(message)
            
            
        
user_One = Admin("damani", "holland", "daho", "damanirayholland@gmail.com")
user_Two = User('amiri', 'aje', 'amaj', 'amiri.aje@gmail.com')

user_One.describe_user()
user_One.greet_user()
user_One.describe_privileges()



user_Two.describe_user()
user_Two.greet_user()
