import matplotlib.pyplot as plt
import numpy as np
import colormap as cm
import random_walker as rw


num_walkers = 4
T = np.linspace(100,1000,num_walkers) # Temperature
num_steps = 1000

#print(x_data[:, 0])

x, y, v = rw.rand_walker_data(
    100,            # Bounds for plot
    T,              # Temperature array
    num_steps,      # Number of steps
    num_walkers)    # Number of walkers




temperatures = [0, 10, 20, 20]

fig, ax = plt.subplots(nrows=1, ncols=1)
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
fig, ax1 = plt.subplots( figsize = (15,10) , dpi = 75)
ax1.clear()
ax1.cla()

for i in range(num_walkers):
    # We truncate the arrays to prevent the "weird bug", that Christian cannot figure out. It's all his fault really...
    color_list = cm.color_assign(v[:,i], cm.FindPalette(5, 15, temperatures[i]))
    plt.scatter(
        x[:,i][:num_steps - 1], 
        y[:,i][:num_steps - 1], 
        s = 10,
        c = np.array(color_list)[:num_steps - 1], 
        alpha= 0.5)

plt.tick_params(
    axis='both', 
    which='both', 
    bottom='off', 
    top='off', 
    labelbottom='off', 
    right='off', 
    left='off', 
    labelleft='off')
ax = plt.gca()

ax.set_facecolor('xkcd:grey')

fig.patch.set_facecolor('xkcd:grey')

plt.show()



'''
color_list = cm.color_assign(v[:,0], cm.FindPalette(5, 15) )
plt.scatter(x[:,0], y[:,0], c = color_list)
plt.show()
'''
