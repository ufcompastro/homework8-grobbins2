#code by Grady Robbins

import numpy as np

Ti = 0 # C
Tenv = 40 #C
time = 10 #min
#dT/dt = -K(T-Tenv)
K = .001 #cooling coefficient in /s
def f(T,t):
    return -1*K*(T-Tenv)
#using analytic methods and integrating, setting T=0 when t = 0, T = e^-Kt*(-Tenv) + Tenv, after 10 minutes T = 18.05C
print("using analytic methods, integrating, and setting T=0 when t = 0, T = (e^-Kt)*(-Tenv) + Tenv. after 10 minutes (600s) T = 18.0475C")
print("")
print("using Euler's method:")
timestep_array = [1,0.5,0.25,0.125] #testing timesteps
#euler's method
Final_temps = []
for h in timestep_array:
    T = 0 #at t = 0, initial condition
    T_of_han = []
    timestep = np.arange(0,600,h)
    for time in timestep:
        T = T + h*f(T,time) #euler's method
        T_of_han.append(T)
    Final_temps.append(T_of_han[-1])
for n in range(len(timestep_array)):
    print("using a timestep of",timestep_array[n]," seconds, the final temperature after 10 minutes is",Final_temps[n],"using Euler's method, which has an error of",(Final_temps[n]-18.0475)/.180475,"%")
print("")
#runge-Cutta method
Final_temps_runge = []
for h in timestep_array:
    T = 0 #at t = 0, initial condition                                                                                                          
    T_of_han = []
    timestep = np.arange(0,600,h)
    for time in timestep:
        k1 = h*f(T,time)
        k2 = h*f(T+0.5*k1,time+0.5*h)
        T = T + k2 #euler's method                                                                                                  
        T_of_han.append(T)
    Final_temps_runge.append(T_of_han[-1])
print("using Runge-Cutta method:")
for n in range(len(timestep_array)):
    print("using a timestep of",timestep_array[n]," seconds, the final temperature after 10 minutes is",Final_temps_runge[n],"using Runge-Cutta method, which has an error of",(Final_temps_runge[n]-18.0475)/.180475,"%")
print('')
print("the error decreases as timestep decreases, and Runge-Cutta method is much more accurate than Euler")
