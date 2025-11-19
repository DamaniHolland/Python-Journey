###############################################################################
#   Damani Holland
#   11/18/2025
#   CS Python
###############################################################################


'''

5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
as 1st or 2nd . Most ordinal numbers end in th, except 1, 2, and 3 .

•  Store the numbers 1 through 9 in a list .

•  Loop through the list .

•  Use an if-elif-else chain inside the loop to print the proper ordinal end-
ing for each number . Your output should read "1st 2nd 3rd 4th 5th 6th 
7th 8th 9th", and each result should be on a separate line

'''

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    th_ending = [4, 5, 6, 7, 8, 9,]
    nd_ending = [2]
    st_ending = [1]
    rd_ending = [3]
    number_index = numbers.index(number)
    if number_index in th_ending:
        print(str(number) + "th")
    elif number_index in nd_ending:
        print(str(number) + "nd")
    elif number_index in st_ending:
        print(str(number) + "st")
    elif number_index in rd_ending:
        print(str(number) + "rd")
    else:
        print(str(number))