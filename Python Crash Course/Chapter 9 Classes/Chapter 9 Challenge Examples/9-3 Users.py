###############################################################################
#   Damani Holland
#   12/28/2025
#   CS Python
###############################################################################

'''

9-3. Users: Make a class called User . Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile . Make a method called describe_user() that prints a summary 
of the user’s information . Make another method called greet_user() that prints 
a personalized greeting to the user .Create several instances representing different 
users, and call both methods for each user .

'''

class User():
    
    def __init__(self, gender, first_name, last_name, date_of_birth, occupation):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.dob = date_of_birth
        self.occupation = occupation
    
    def describe_user(self):
        print("\nGender: " + self.gender.title())
        print("First Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("D.O.B: " + self.dob)
        print("Occupation: " + self.occupation.title())
        
    def greeting(self):
        print("\nWelcome " + self.first_name.title())
        print("Your account has been created with the information entered: ")
        
user_01 = User('male', 'damani', 'holland', 'July 5th, 1998', 'grocery')
user_01.greeting()
user_01.describe_user()

user_02 = User('female', 'amiri', 'aje', 'June 22nd 1998', 'real estate manager')
user_02.greeting()
user_02.describe_user()
