###############################################################################
#   Damani Holland
#   7/9/2026
#   CS Python
###############################################################################

"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178) . 
Store the classes User, Privileges, and Admin in one module . Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that 
everything is working correctly.
"""


from User_Module import Admin

user_One = Admin('nexus', 'drift', 'thenexusdrift@gmail.com', 3105842085, "March 25, 1998")

user_One.greet_user()
user_One.describe_user()
user_One.show_privileges()