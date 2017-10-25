#!/usr/bin/env python

#To use this program from the command line -
#input: python Exam1SupUser1.py Supa.txt

import importlib
from scipy import integrate
import numpy as np
import os, sys
import matplotlib as plot
from pylab import *




f=open(sys.argv[1],'r')
file = open('Sup1.txt','w')

data = f.readlines()
Vs = float(data[3])  # voltageSource
R = float(data[9])
L = float(data[7])
C = float(data[5])

print(Vs,R,L,C)


file.write("The response of the circuit is: \n")

if float(C>((4*L)/(R**2))):
    file.write('Overdamped\n')
elif float(C==4*L/R**2):
    file.write('Critically damped\n')
else:
    file.write('UnderDamped\n')

def rlc(A,t):
    Vc,s=A   #prepares equation for array used in res
    
    res=np.array([s,(Vs-Vc-(R*C*s))/(L*C)]) #ODE in terms of voltage observed at the Capacitor
    
    return res

time=np.linspace(0.0,0.5e-6,1000) #array of time intervals

vc,s = integrate.odeint(rlc,[0.0,0.0],time).T  #(function,initial values,time)

i=1.0e-9*s #current

figure('Voltage vs Time')
file.write('Current Data: \n')
#file.write(str(i))
plot(time,vc)
xlabel('t')
ylabel('Vc')
savefig('Voltage vs Time(user input).png')
show()

