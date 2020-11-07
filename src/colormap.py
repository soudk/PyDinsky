# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib as plt
import seaborn as sns

#import temperature of the day
temp

#temperature range limits
cold_to_mid = 5
mid_to_warm = 15

hot_pal = [
    [1, .2, .3],
    [1, .3, .23],
    [1, .4, .15],
    [1, .5, .08],
    [1, .5, 0]
    ]

med_pal = [
    [.4, 1, .6],
    [.55, 1, .5],
    [.7, 1, .4],
    [.85, 1, .3],
    [1, 1, .2]
    ]

cold_pal = [
    [0, 0, .8],
    [.15, .25, .85],
    [.3, .5, .9],
    [.45, .75, .95],
    [.6, 1, 1]
]

"""
cold_pal = sns.color_palette()
med_pal = sns.color_palette()
hot_pal = sns.color_palette()
"""

palettes = [cold_pal, med_pal, hot_pal]

def FindPalette(temp, cold_to_mid, mid_to_warm):
    if temp<cold_to_mid:
        return palettes[0]
    if cold_to_mid<=temp and temp<mid_to_warm:
        return palettes[1]
    if mid_to_warm<=temp:
        return palettes[3]

my_pal = FindPalette(temp, cold_to_mid, mid_to_warm)



def color_assign(velocities, color_palette):
    '''Takes an array with velocities for all of the particle and outputs the colours mathcing the velocities. '''
    
    nb_velo = len(velocities)       # Number of elements in the array containing the velocities
    nb_color = len(color_palette)   # Number of color in the palette
    min_velo = min(velocities)
    max_velo = max(velocities)
    interval = (max_velo - min_velo))/nb_color

    ranges = # Array containing [min_bound, max_bound, color

    for i in range(nb_color):
        ranges.append(
            [ min(velocities) + interval * i ,          # Minimum bound 
            min(velocities) + interval * (i + 1) ,      # Maximum bound
            color_palette[i]                            # RGB Colour Code for the interval
            )


    color_list = []

    for i in velocities:
        for j in ranges:
            if i > j[0] and i <= j[1]:
                color_list.append(j[3])

    return color_list