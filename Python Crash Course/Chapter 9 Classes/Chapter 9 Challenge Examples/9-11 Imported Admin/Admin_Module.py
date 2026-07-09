###############################################################################
#   Damani Holland
#   7/9/2026
#   CS Python
###############################################################################
from User_Module import User

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
        message += "\n\t" + str(self.privileges)
        
        print(message)