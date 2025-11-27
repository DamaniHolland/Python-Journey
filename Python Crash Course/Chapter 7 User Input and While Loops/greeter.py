###############################################################################
#   Damani Holland
#   11/25/2025
#   CS Python
###############################################################################

'''

Write Clear Prompts

    - You should include a clear, easy-to-follow prompt that tells the user
      exactly what kind of information you're looking for. Any statement that 
      tells the user what to enter should work.

'''

    # store string inside promt variable
    # add new string to prompt variable


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

    # store input in variable in 'name'
    # print string statement and input statement

name = input(prompt)
print("Hello, " + name + "!")