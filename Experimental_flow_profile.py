# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:38:03 2022

@author: hk3rr
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel(r"C:\Users\hk3rr\Desktop\University stuff\Year 2\CIV2300 - Pipes and Open Channel Hydraulics\Spring Coursework\Flow profiles for python.xlsx")
XDistanceD = pd.DataFrame(data, columns= ['X distance (mm)'])
XDistancemm = XDistanceD.to_numpy(dtype='float', na_value=np.nan)
NegXDistancem = XDistancemm*-10**-3

HeightD = pd.DataFrame(data, columns= ['Height (mm)'])
Heightmm = HeightD.to_numpy(dtype='float', na_value=np.nan) 
Heightm = Heightmm*10**-3

plt.plot(NegXDistancem,Heightm)

plt.xlabel('Horizontal distance (m)')
plt.ylabel('Water level (m)')
plt.title('Graph showing experimentally derived flow profiles')

plt.xlim([-5,0])
plt.ylim([0, 0.2])