
#import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------

class walker: # Input is boltz rand. variable
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.v = 0.0
	def take_step(self,v,xx,yy):	
		self.v = v
		t = np.random.rand()*2*np.pi
		x_step = np.cos(t)
		y_step = np.sin(t)
		self.x += v*x_step
		if self.x < xx[0] or self.x > xx[1]:
			self.x -= 2*v*x_step		
		self.y += v*y_step
		if self.y < yy[0] or self.y > yy[1]:
			self.y -= 2*v*y_step		
	def sample(self):
		return [self.x,self.y,self.v]
#	def intx	

def rand_b(T): # n is number of steps. T is temp

	#c = 4.8*10**(-4) # m/k_b for He
	c = 3.3693*10**(-3) #m/k_b for N2
	def boltz(v,T):
		return (c*v/T)*np.exp(-c*v*v/2*T)
		
	v_mp = np.sqrt(2*c*T) # most probable velocity
	x = np.random.rand()*v_mp*4. # setting max v value as 4 times most probable
	y = np.random.rand()*1.2*boltz(v_mp,T) # setting max y limts as just little above the max of pdf
	if boltz(x,T)>y:
		return x # scaling the x-scale to allow use of integral steps
	else:
		return rand_b(T)

def rand_walker_data(n,T,n_steps,num_walkers): # n=number of walkers, T= temperature

	x = [0,n] # sets range for x
	y = [0,n] # sets range for y
	wlk = [] # init array of walkers
	for i in range(int(num_walkers**0.5)):
		for j in range(int(num_walkers**0.5)):
			wlk.append(walker((i+1)*(max(x)-min(x))/(num_walkers**0.5+1),(j+1)*(max(y)-min(y))/(num_walkers**0.5+1)))
	pos_x = []
	pos_y = []
	vel = []

	for i in range(n_steps):
		temp_x = np.zeros(num_walkers)
		temp_y = np.zeros(num_walkers)
		temp_z = np.zeros(num_walkers)
		for j in range(num_walkers):
			wlk[j].take_step(rand_b(T[j]),x,y)
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

def temp_map(n):
	return np.zeros((n,n))

#----------------------------------------------------------------------------
	
num_walkers = 16
num_steps = 1000
n_grid = 100
T = np.linspace(100,1000,num_walkers) # Temperature
tmap = temp_map(n_grid) 
x,y,v = rand_walker_data(n_grid,T,num_steps,num_walkers)

for i in range(num_walkers):
	plt.plot(x[:,i],y[:,i],'.')
plt.show() 

#-------------------------------------------------------------------------
