###############################################################################
#   Damani Holland
#   4/24/2025
#   CS Python
###############################################################################

# 2-7 Stripping Names

'''
Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''

name1 = ' Damani '
name2 = ' Craig '

print('Original:' + name1 + name2)
print('.lstrip():' + name1.lstrip() + name2.lstrip())
print('.rstrip():' + name1.rstrip() + name2.rstrip())
print('.strip():' + name1.strip() + name2.strip())