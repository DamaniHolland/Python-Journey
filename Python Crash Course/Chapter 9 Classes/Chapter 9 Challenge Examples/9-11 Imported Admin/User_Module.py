###############################################################################
#   Damani Holland
#   7/9/2026
#   CS Python
###############################################################################
class User():
    
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth):
        self.first_name  = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth

    def describe_user(self):
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        phone_number = self.phone_number
        date_of_birth = self.date_of_birth

        message = "\nUser Imformation:"
        message += "\n\tFirst name: " + first_name.title()
        message += "\n\tLast name: " + last_name.title()
        message += "\n\tEmail: " + email
        message += "\n\tPhone number: " + str(phone_number)
        message += "\n\tDate of Birth: " + date_of_birth
        
        print(message)

    def greet_user(self):
        first_name = self.first_name
 
        message = "\nWelcome " + first_name.title() + "!"
        
        print(message)
        
class Privileges():
    
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges
        
        
    def show_privileges(self):
        message = "\nAdmin Privileges:"
        message += "\n\t" + str(self.privileges)
        
        print(message)

class Admin(User):
    
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth):
        super(Admin, self).__init__(first_name, last_name, email, phone_number, date_of_birth)
              
        self.privileges = Privileges()
    
    
    def __init__(self, first_name, last_name, email, phone_number, date_of_birth):
        super(Admin, self).__init__(first_name, last_name, email, phone_number, date_of_birth)
        
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        message = "Admin Privileges:"
        message += "\n\t" + self.privileges
        
        print(message)