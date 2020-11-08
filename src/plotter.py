import matplotlib.pyplot as plt
import numpy as np
import colormap as cm

import os
os.chdir('..') 
import random_walkers as rw


x_data, y_data, velocities = rw.rand_walker_data(4, 100)
print(x_data[:, 0])


T = 1000.0 # Temperature
num_walkers = 4
x,y,v = rw.rand_walker_data(num_walkers,T)

temperatures = [0, 10, 20, 20]

for i in range(num_walkers):
    color_list = cm.color_assign(v[:,i], cm.FindPalette(5, 15, temperatures[i]))
    plt.scatter(
        x[:,i], 
        y[:,i], 
        s = 100,
        c = np.array(color_list), 
        alpha= 0.2)

plt.tick_params(
    axis='both', 
    which='both', 
    bottom='off', 
    top='off', 
    labelbottom='off', 
    right='off', 
    left='off', 
    labelleft='off')

plt.show()



'''
color_list = cm.color_assign(v[:,0], cm.FindPalette(5, 15) )
plt.scatter(x[:,0], y[:,0], c = color_list)
plt.show()
'''
