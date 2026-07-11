###############################################################################
#   Damani Holland
#   7/10/2026
#   CS Python
###############################################################################
# Reading an Entire File
file_name = 'Python Crash Course\Chapter 10 Files and Exceptions\pi_digits.txt'
""" We store the name of the file we're reading from in the variable 'file_name' """
with open(file_name) as file_object:
    """ Use 'with' syntax to let Python open and close the file properly."""
    contents = file_object.read()
    print(contents.rstrip())


# Reading Line by Line
with open(file_name) as file_object:
    for line in file_object:
        """Use 'for to work through each line in the file by looping over the 
            file object.
        """
        print(line.rstrip()) 
        """print each line using '.rstrip'""" 
        # Using '.rstrip()'on each line in the print                  
        # statement eliminates these extra blank lines
        
# Making a list of lines from a file