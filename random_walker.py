import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

class walker: # Input is boltz rand. variable
	def __init__(self,x=0.0,y=0.0,v=0.0):
		self.x = x
		self.y = y
		self.v = v
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

def boltz(v,T):
	c = 4.8*10**(-4) # m/k_b
	return (c*v/T)*np.exp(-c*v*v/2*T)

T = 1000.0 # Temperature

z = [] # array of random variable (boltzmann-velocity) 
n = 10000 # no. of steps

for i in range(n):
	x = np.random.rand()*10.
	y = np.random.rand()*5./10**7
	if boltz(x,T)>y:
		z.append([x,y]) 
z = np.asarray(z)

plt.scatter(z[:,0],z[:,1])
plt.xlim(0,10)
plt.ylim(0,5/10**7)
plt.show()

num_walkers = 1
w = walker()
pos = []
for i in range(len(z)):
	w.take_step(z[i,0])
	pos.append(w.sample())

pos= np.asarray(pos)
plt.plot(pos[:,0],pos[:,1])
plt.show()
