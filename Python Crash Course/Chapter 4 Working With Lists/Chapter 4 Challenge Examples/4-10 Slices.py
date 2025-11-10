###############################################################################
#   Damani Holland
#   11/10/2025
#   CS Python
###############################################################################


'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:

•  Print the message, The first three items in the list are: . Then use a slice to 
print the first three items from that program’s list .

•  Print the message, Three items from the middle of the list are: . Use a slice 
to print three items from the middle of the list .

•  Print the message, The last three items in the list are: . Use a slice to print 
the last three items in the list
'''

cubes = []

for number in range(1,11):
    cubes.append(number**3)
print(cubes)
    
print("\nThe first three items on the list are:")
print(cubes[:3])

print("\n Three items from the middle of the list are:")
print(cubes[4:7])

print("\nThe Last three items on the list are:")
print(cubes[-3:])