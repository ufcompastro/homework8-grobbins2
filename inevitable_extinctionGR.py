#Code by Grady Robbins
import matplotlib.pyplot as plt
import numpy as np
#define predator and prey functions, x represents rabbits and y represents foxes
#dx/dt = ax - Bxy    dy/dt = Yxy - py
alpha = 1
beta,gamma = .5,.5
epsilon = 2
#r is a function of x,y
def f(r,t):
    x =r[0]
    y =r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y - epsilon*y
    fr = np.array([fx,fy],float)
    return fr
# xi = yi = 2
h = .01 #timestep
time_tot = 30
xi = 2
yi = 2
time = np.arange(0,30,h)
x_end=[]
y_end=[]
r = np.array([xi,yi],float) #set up 4th order runge-cutta
for t in time:
    x_end.append(r[0])
    y_end.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+.5*k1,t+.5*h)
    k3 = h*f(r+.5*k2,t+.5*h)
    k4 = h*f(r+k3,t+h)
    r = r + (k1 + 2*k2 + 2*k3 + k4)/6
print("the starting rabbit and fox populations are 2 and 2")
print("after a time period of 0-30, the ending rabbit and fox populations are",x_end[-1],y_end[-1],"respectively")
plt.plot(time,x_end, label = 'rabbits')
plt.plot(time,y_end, label = 'foxes')
plt.legend()
plt.savefig('inevitable_infinity.png')
print("after observing the plot of foxes and rabbits over time, it appears that they are in and endless cycle of birth and death, with peaks slightly offset.")
print('this makes sense as if the foxes eat too many rabbits, the rabbit population will decrease causing less food for foxes, so the fox population closely follows the rabbit population')
print('')
print("will they ever escape this eternal hell? what is their purpose of existence? Can it ever end? Perhaps we shouldn't have opened this can of worms.")
