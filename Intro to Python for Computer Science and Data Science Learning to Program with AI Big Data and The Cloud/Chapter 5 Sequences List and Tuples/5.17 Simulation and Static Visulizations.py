###############################################################################
#   Damani Holland
#   4/9/2025
#   CS Python 121
###############################################################################

# 5.17.2 Visualizing Die-Roll fequencies and Percentages

# Importing the Libraries

import matplotlib.pyplot as plt

import numpy as np

import random

import seaborn as sns

'''
- Matplotlib.pylot as plt contains the matplotlib library's graphing capabilities
- Nunpy library includes the function unique that we'll use to summarize the die rolls. 
- Random module contains the seaborn library's graphing capabilities we use
'''

# Rolling the Die and Calculating Die Frequencies

'''
Numpy's '.unique()' function determines the unique roll values and their frequencies
'''
rolls = [random.randrange(1, 7) for i in range(600)] # generates a random number between 1 and 6 600 times
values, frequencies = np.unique(rolls, return_counts = True) # .unique(rolls) will a list of all numbers that appear in sequence
                                                            # .unique(return_counts = True) return the number of times each unique number appears


'''
Creating initial Bar Plot
'''

title = f'Rolling a Six-Sided Die {len(rolls):,} Times'

sns.set_style('whitegrid')

axes = sns.barplot(x = values, y = frequencies, palette = 'bright')

'''
Setting the Window Title and Labeling
'''

axes.set_title(title) 
'''
Uses the axes object's '.set_title()' to display the title string centered 
above the plot. This method returns a Text object containing the 
title ('Die Value', 'Frequency') and its location('xlabel', 'ylabel')
'''

axes.set(xlabel = 'Die Value', ylabel = 'Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
    

