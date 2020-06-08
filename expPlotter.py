# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:07:23 2020

@author: Dale
"""

def expPlotter(values,proteins,labels,title,std):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    
    x = np.arange(len(proteins))  # the label locations
    width = 0.5  # the width of the bars
    diff = width/len(labels)
    num = len(labels)
    if (num % 2) == 0:
        shift = num/2
        partition = np.arange(num)
        partition = partition - shift
    else:
        shift = num/2-0.5
        partition = np.arange(num)
        partition = partition - shift
    fig, ax = plt.subplots()
    
    for i in range(len(labels)):
        rects1 = ax.bar(x + partition[i]*diff,values[i,:],diff,label = labels[i],yerr=std[i,:],
       align='center',
       alpha=1,
       ecolor='black',
       capsize=4)
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('y-label',fontname="Arial", fontsize=12)
    ax.set_xlabel('x-label',fontname="Arial", fontsize=12)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(proteins)
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    ax.legend()
    fig.tight_layout()
    
    plt.show()