# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:11:33 2022

@author: hk3rr
"""
import numpy as np

inflow1 = 0.00833333
inflow2 = 0.0111111
inflow3 = 0.00972222
inflow4 = 0 

Reslength = 4.7
Reswidth = 0.31
Maxresdepth = 0.375
Wierstart = 0.211
g = 9.81
Cd = 0.7 #? Coefficient of discharge

Qin = inflow2
Resarea = Reslength*Reswidth

b = np.arange(0,0.3,0.005)

h = np.arange(0,0.3,0.005)

Deltadepths = []
Areas = []
haitches = []

for bi in b:
    for hi in h:
        
            Qout = (2/3)*Cd*bi*((2*g)**0.5)*(hi**(2/3))

            Deltadepth = (Qin - Qout) / Resarea
            
            Deltadepths.append(Deltadepth)
            Areas.append(bi*hi)
            haitches.append(bi)
    
    
def remove_pos(l):
    return [e for e in l if e > 0]
    
remove_pos(Deltadepths)


