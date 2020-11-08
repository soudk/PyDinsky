# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib as plt
import seaborn as sns
import numpy as np
#import get_temperature as get_t
import random as ran



#temperature range limits
cold_to_mid = 278.15
mid_to_warm = 293.15

random_range = 0.1

hot_pal = [
    [1 - ran.uniform(0, random_range), .2 + ran.uniform(0, random_range), .3 + ran.uniform(0, random_range)],
    [1 - ran.uniform(0, random_range), .3 + ran.uniform(0, random_range), .23 + ran.uniform(0, random_range)],
    [1 - ran.uniform(0, random_range), .4 + ran.uniform(0, random_range), .15 + ran.uniform(0, random_range)],
    [1 - ran.uniform(0, random_range), .5 + ran.uniform(0, random_range), .08 + ran.uniform(0, random_range)],
    [1 - ran.uniform(0, random_range), .5 + ran.uniform(0, random_range), 0 + ran.uniform(0, random_range)]
    ]

med_pal = [
    [.4 + ran.uniform(0, random_range), 1 - ran.uniform(0, random_range), .6 + ran.uniform(0, random_range)],
    [.55 + ran.uniform(0, random_range), 1 - ran.uniform(0, random_range), .5 + ran.uniform(0, random_range)],
    [.7 + ran.uniform(0, random_range), 1 - ran.uniform(0, random_range), .4 + ran.uniform(0, random_range)],
    [.85 - ran.uniform(0, random_range), 1 - ran.uniform(0, random_range), .3 + ran.uniform(0, random_range)],
    [1 - ran.uniform(0, random_range), 1 - ran.uniform(0, random_range), .2 + ran.uniform(0, random_range)]
    ]

cold_pal = [
    [0 + ran.uniform(0, random_range), 0 + ran.uniform(0, random_range), .8 - ran.uniform(0, random_range)],
    [.15 + ran.uniform(0, random_range), .25 + ran.uniform(0, random_range), .85 - ran.uniform(0, random_range)],
    [.3 + ran.uniform(0, random_range), .5 + ran.uniform(0, random_range), .9 - ran.uniform(0, random_range)],
    [.45 + ran.uniform(0, random_range), .75 - ran.uniform(0, random_range), .95 - ran.uniform(0, random_range)],
    [.6 + ran.uniform(0, random_range), 1 - ran.uniform(0, random_range), 1 - ran.uniform(0, random_range)]
]

"""
cold_pal = sns.color_palette()
med_pal = sns.color_palette()
hot_pal = sns.color_palette()
"""

def FindPalette(temp):
    #temp = get_t.get_temperature()
    palettes = [cold_pal, med_pal, hot_pal]

    if temp<cold_to_mid:
        return palettes[0]
    if cold_to_mid<=temp and temp<mid_to_warm:
        return palettes[1]
    if mid_to_warm<=temp:
        return palettes[2]




def color_assign(velocities, color_palette):
    '''Takes an array with velocities for all of the particle and outputs the colours mathcing the velocities. '''
    
    nb_velo = len(velocities)       # Number of elements in the array containing the velocities
    nb_color = len(color_palette)   # Number of color in the palette
    min_velo = min(velocities)
    max_velo = max(velocities)
    interval = (max_velo - min_velo)/nb_color

    ranges = []
    ranges.append(
        [ min(velocities)-0.0001 ,          # Minimum bound 
        min(velocities) + interval  ,      # Maximum bound
        color_palette[0] ]                          # RGB Colour Code for the interval
        )

    for i in range(nb_color - 1):
        ranges.append(
            [ min(velocities) + interval * (i + 1) ,          # Minimum bound 
            min(velocities) + interval * (i + 2) ,      # Maximum bound
            color_palette[(i+1)] ]                          # RGB Colour Code for the interval
            )


    color_list = []

    for velo in velocities:
        for j in ranges:
            if velo > j[0] and velo <= j[1]:
                color_list.append(j[2])

    return color_list

