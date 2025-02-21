# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:00:35 2022

@author: hk3rr
"""
import numpy as np
import matplotlib.pyplot as plt

g = 9.81#ms^-2      gravity

SpillWidth = 0.31#m   Width of the spillway

Q = 0.009861#m3^s^-1

n = 0.012#     Gauckler-Manning coefficient

S0 = 0.0025

yc = (((Q/SpillWidth)**2)/g)**(1/3)

yn = 0.06131

Esc = (3/2)*yc

y1 = np.arange(0.016,yc,0.0001) #m

Cd = 0.8

"""
Upstream starts here
"""

A = []#m  Hydraulic area of spillway
P = []#m^2
R = []#m Hydraulic radius of spillway
V = []#ms^-1   Velocity of flow
Sf = [] 
Fr = []
S0_Sf = []
Es = []
dEs = []
Sfavg = []
dx = []
x = [0]
Bed = []
BedAndSurface = []
Head = []
yns = []
ycs = []
SeqDepth = []


for i in range(len(y1)):
    
    A.append(y1[i]*SpillWidth)
    
    R.append( A[i] / (2 * y1[i] + SpillWidth) )
    
    V.append( Q/A[i] )
    
    Sf.append( (n**2*V[i]**2)/R[i]**(4/3) )
    
    Fr.append( V[i]/((g*y1[i])**0.5) )
    
    Es.append( y1[i] + ((V[i]**2)/(2*g)) )
    
    dEs.append( Es[i]-Es[i-1] )
    
    Sfavg.append((Sf[i]+Sf[i-1])/2)
    
    dx.append( dEs[i] / (S0-Sfavg[i]) )
    
    x.append( x[i]-dx[i] )
    
    Bed.append( S0*x[i])
    
    SeqDepth.append( (y1[i]/2)*(((1+(8*(Fr[i]**2)))**0.5)-1) )
    
x.pop(len(y1))

fig, ax = plt.subplots()

ax.plot(x, y1,label='Upstream profile')
ax.plot(x, SeqDepth,'-.',label='Sequential depth')

"""
#Downstream starts here
"""

H = (Q/(1.705*Cd*SpillWidth))**(2/3)

y2 = np.arange(H,yn,-0.0001) #Downstream calculation range

#yn = H

A = []#m  Hydraulic area of spillway
P = []#m^2
R = []#m Hydraulic radius of spillway
V = []#ms^-1   Velocity of flow
Sf = [] 
Fr = []
S0_Sf = []
Es = []
dEs = []
Sfavg = []
dx = []
x = [-5.16]
Bed = []
BedAndSurface = []
Head = []
yns = []
ycs = []
SeqDepth = []

for i in range(len(y2)):
    
    A.append(y2[i]*SpillWidth)
    
    R.append( A[i] / (2 * y2[i] + SpillWidth) )
    
    V.append( Q/A[i] )
    
    Sf.append( (n**2*V[i]**2)/R[i]**(4/3) )
    
    Fr.append( V[i]/((g*y2[i])**0.5) )
    
    S0_Sf.append( S0 - Sf[i] )
    
    Es.append( y2[i] + ((V[i]**2)/(2*g)) )
    
    dEs.append( Es[i]-Es[i-1] )
    
    Sfavg.append((Sf[i]+Sf[i-1])/2)
    
    dx.append( dEs[i] / (S0-Sfavg[i]) )
    
    x.append( x[i]-dx[i] )
    
    Bed.append( S0*x[i])
    
    BedAndSurface.append(Bed[i]+y2[i])
    
    yns.append(yn+Bed[i])
    
    ycs.append((((Q/SpillWidth)**2)/g)**(1/3)+Bed[i])
    
    Head.append(Es[i]+Bed[i])
    
    SeqDepth.append( (y2[i]/2)*(((1+(8*(Fr[i]**2)))**0.5)-1) )
    
x.pop(len(y2))

ax.plot(x, Bed, label='Bed')
ax.plot(x, y2, label='Downstream profile')
ax.plot(x,ycs,'--', label='yc')
ax.plot(x,yns,'--',label='yn')

plt.xlim([-5.160,0])
plt.ylim([-0.02, 0.2])

ax.grid(True,'major')
ax.grid(True,'minor')
leg = ax.legend(loc='upper right');

plt.xlabel('Horizontal ditance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Graph showing theoretically derived flow profiles')
