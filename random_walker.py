
#import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------

class walker: # Input is boltz rand. variable
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.v = 0.0
	def take_step(self,v):	
		self.v = v
		t = np.random.rand()*2*np.pi
		x_step = np.cos(t)
		y_step = np.sin(t)
		self.x += v*x_step
		self.y += v*y_step
	def sample(self):
		return [self.x,self.y,self.v]
#	def intx	

def rand_b(n,T): # n is number of steps. T is temp

	#c = 4.8*10**(-4) # m/k_b for He
        c = 3.3693*10**(-3) #m/k_b for N2
	def boltz(v,T):
		return (c*v/T)*np.exp(-c*v*v/2*T)
		
	z = [] # array of random variable (boltzmann-velocity) 
	v_mp = np.sqrt(2*c*T)
	for i in range(n):
		x = np.random.rand()*v_mp*4. # setting max v value as 4 times most probable
		y = np.random.rand()*1.2*boltz(v_mp,T) # setting max y limts as just little above the max of pdf
		if boltz(x,T)>y:
			z.append([x,y]) 
	z = np.asarray(z)
	return z[:,0] # scaling the x-scale to allow use of integral steps

def rand_walker_data(n,T): # n=number of walkers, T= temperature

	x = [0,100] # sets range for x
	y = [0,100] # sets range for y
	wlk = [] # init array of walkers
	for i in range(int(num_walkers**0.5)):
		for j in range(int(num_walkers**0.5)):
			wlk.append(walker((i+1)*(max(x)-min(x))/5,(j+1)*(max(y)-min(y))/5))
	pos_x = []
	pos_y = []
	vel = []
	z = rand_b(1000,T) # Generates array of random variables
	
	for i in range(len(z)):
		temp_x = np.zeros(num_walkers)
		temp_y = np.zeros(num_walkers)
		temp_z = np.zeros(num_walkers)
		for j in range(num_walkers):
			wlk[j].take_step(z[i])
			temp_x[j] = wlk[j].x
			temp_y[j] = wlk[j].y
			temp_z[j] = wlk[j].v
		pos_x.append(temp_x)
		pos_y.append(temp_y)
		vel.append(temp_z)	
	pos_x = np.asarray(pos_x)
	pos_y = np.asarray(pos_y)
	vel   = np.asarray(vel)
	return pos_x, pos_y, vel

#----------------------------------------------------------------------------

T = 1000.0 # Temperature
num_walkers = 16
x,y,v = rand_walker_data(num_walkers,T)

for i in range(num_walkers):
	plt.plot(x[:,i],y[:,i],'.')
plt.show() 

#----------------------------------------------------------------------------

