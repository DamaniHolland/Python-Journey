###############################################################################
#   Damani Holland
#   12/08/2025
#   CS Python
###############################################################################

'''

8-2. Favorite Book: Write a function called favorite_book() that accepts one 
parameter, title . The function should print a message, such as One of my 
favorite books is Alice in Wonderland . Call the function, making sure to 
include a book title as an argument in the function call.

'''

def favorite_book(book_title):
    print(book_title.title() + " is one of my favorite books.")
    
favorite_book("Of Mice and Men")