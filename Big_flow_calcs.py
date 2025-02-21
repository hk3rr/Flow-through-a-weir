# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:25:44 2022

@author: hk3rr
"""
import numpy as np
import matplotlib.pyplot as plt

WeirWidth = 210*10**-3#m
WeirHeight = 76*10**-3#m

DischargeCoeff = 0.6

Time = np.arange(0,101,1)

PlanArea = 1.457#m^2

OverflowDepth = 0.375#m

BedToWeir = OverflowDepth-WeirHeight #m

Inflow1 = 0.008333333#m^3s^-1
Inflow2 = 0.011111111#m^3s^-1
Inflow3 = 0.009722222#m^3s^-1
Inflow4 = 0

Depth = [0] #m             Reservoir Depth
HeightAboveWeir = [] #m    Height above weir that reservoir is at
Outflow = [] #m^3s^-1      Rate of water flowing out of reservoir through weir
ResChange = [] #m^3s^-1    Rate of change of water in reservoir
HeightChange = [] #ms^-1   Rate of reservoir water level change
Inflows = [] #m^3s^-1      Inflows :)

def OutflowCalc(a,b,c):    #a=HeightAboveWeir , b=DischargeCoeff, c=WeirWidth
    if a > 0:
        output = ((2/3)*b*c*((2*9.81)**0.5)*a**(3/2))
    else: 
        output = (0)
    return output

for i in Time:
    HeightAboveWeir.append(Depth[i]-BedToWeir)
    if i<31:
        Inflows.append(Inflow1)
    else:
        if i<61:
            Inflows.append(Inflow2)
        else:
            if i<91:
                Inflows.append(Inflow3)
            else: 
                Inflows.append(Inflow4)
                
    Outflow.append(OutflowCalc(HeightAboveWeir[i],DischargeCoeff,WeirWidth))    
    ResChange.append(Inflows[i]-Outflow[i])
    HeightChange.append(ResChange[i]/PlanArea)
    Depth.append(Depth[i]+HeightChange[i])
    
Depth.pop(101)

#print(sum(Outflow))
#print(max(Depth))

#plt.plot(Time,Depth)
#plt.plot(Time,Outflow)
#plt.plot(Time,Inflows)
#plt.plot(Time,ResChange)

"""
Inflows
"""
plt.figure(2)
plt.plot(Time,Inflows)

plt.title("Time and Inflow to Reservoir plot")
plt.xlabel("Time (s)")
plt.ylabel("Inflow (m^3s^-1)")

plt.xlim([0,105])
plt.ylim([0,0.0115])

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')
plt.show()
"""
Outflow
"""
plt.figure(0)
plt.plot(Time, Outflow)

plt.title("Time and Outflow from Reservoir plot")
plt.xlabel("Time (s)")
plt.ylabel("Outflow (m^3s^-1)")

plt.xlim([0,105])
plt.ylim([0,0.0115])

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')
plt.show()
"""
Depth
"""
plt.figure(1)
plt.plot(Time,Depth)

plt.title("Time and Depth of Reservoir plot")
plt.xlabel("Time (s)")
plt.ylabel("Depth (m)")

plt.xlim([0,105])
plt.ylim([0,0.4])

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')
plt.show()