###############################################################################
#   Damani Holland
#   7/7/2026
#   CS Python
###############################################################################
'''

9-8. Privileges: Write a separate Privileges class . The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 9-7 . 
Move the show_privileges() method to this class . Make a Privileges instance 
as an attribute in the Admin class . Create a new instance of Admin and use your 
method to show its privileges

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
        
class Privileges():
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def describe_privileges(self):
        print("List of Privileges: ")
        for privilege in self.privileges:
            message = "\n\t" + privilege
            print(message)
        
class Admin(User):
    
    def __init__(self, first_name, last_name, username, email):
        super(Admin, self).__init__(first_name, last_name, username, email)
        self.privileges = Privileges()
    



        
user_One = Admin("damani", "holland", "daho", "damanirayholland@gmail.com")
user_Two = User('amiri', 'aje', 'amaj', 'amiri.aje@gmail.com')
user_Three = Admin('tchise', 'james', 'tcja', 'j.tchise@gmail.com')

user_One.describe_user()
user_One.greet_user()

user_Two.describe_user()
user_Two.greet_user()

user_Three.greet_user()
user_Three.describe_user()
user_Three.privileges.describe_privileges()