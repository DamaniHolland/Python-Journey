# coding: utf-8
###############################################################################
#   Damani Holland
#   4/9/2025
#   CS Python 121
###############################################################################
import matplotlib.pyplot as plt

import numpy as np

import random

import seaborn as sns

import sys 

rolls = [random.randrange(1, 7) for i in range(int(sys.argv[1]))] # generates a random number between 1 and 6 600 times
values, frequencies = np.unique(rolls, return_counts = True) # .unique(rolls) will a list of all numbers that appear in sequence
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'

sns.set_style('whitegrid')

axes = sns.barplot(x = values, y = frequencies, palette = 'bright')
axes.set_title(title)
axes.set(xlabel = 'Die Value', ylabel = 'Frequency')
axes.set_ylim(top=max(frequencies) * 1.10)
for bar,frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
    
plt.show()

