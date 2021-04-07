import numpy as np
import matplotlib.pyplot as plt

partNum=1     # number of particles
dt=0.005       # time step 
LX=10          # size of container 
LY=10
KK=100.0       # strength of repulsive wall force
EPS=1.0          # strength of particle-particle interaction

x = np.zeros(partNum)   # x cooordinate of particles
y = np.zeros(partNum) 
vx = np.zeros(partNum)  # velocites 
vy = np.zeros(partNum)
ax = np.zeros(partNum)  #accelerations
ay = np.zeros(partNum)


x[0]=1     # initial position (with one particle)
y[0]=2


vx[0]=10   #initial velocity
vy[0]=-5


for i in range (2000):
    
     x[:] = x[:] + vx[:] * dt + (ax[:] * dt**2)/2        #first step of verlet integration
     y[:] = y[:] + vy[:] * dt + (ay[:] * dt**2)/2
     vx[:] = vx[:]+0.5 * ax[:] * dt 
     vy[:] = vy[:]+ 0.5 * ay[:] * dt


     ax[:] = 0
     ay[:] = 0
           
     for j in range (partNum):
         
        if (x[j] > LX):
          ax[j]+=-KK*(x[j]-LX)
        elif (x[j] < 0):
          ax[j]+=-KK*x[j]
       
        if (y[j] > LY):
             ay[j]+=-KK*(y[j]-LY)
        elif (y[j] < 0):
             ay[j]+=-KK*y[j]
             
        for k in range (j+1, partNum):
           dist2 =(x[j] - x[k])**2+(y[j] - y[k])**2
           dist = np.sqrt(dist2)
           dist7=(dist2**3)*dist
           dist13= (dist2**6)*dist
        
           dVdr=12*EPS*(1/dist13-1/dist7)
           aa=dVdr*(x[j] - x[k])/dist
           ax[j] += aa
           ax[k] += -aa
           aa=dVdr*(y[j] - y[k])/dist
           ay[j] += aa
           ay[k] += -aa
           
          
      
     vx[:] = vx[:]+0.5 * ax[:] * dt 
     vy[:] = vy[:]+ 0.5 * ay[:] * dt

     plt.scatter(x,y)

 
plt.show()
   


 

