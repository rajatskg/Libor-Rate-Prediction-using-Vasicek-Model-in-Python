# -*- coding: utf-8 -*-
"""
Created on Tue May 26 01:39:57 2020

@author: Rajat Gupta
website:
https://github.com/jamesmawm/Mastering-Python-for-Finance-source-codes/blob/master/B03898_05_Codes/vasicek.py

"""
"""
README
======
This file contains Python codes.
======
"""

""" Simulate interest rate path by the Vasicek model """
#%%
import numpy as np
from matplotlib.pylab import rcParams 
rcParams['figure.figsize'] = 16,7

def vasicek(r0, K, theta, sigma, T=1., N=10, seed=777):    
    np.random.seed(seed)
    dt = T/float(N)    
    rates = [r0]
    for i in range(N):
        dr = K*(theta-rates[-1])*dt + sigma*np.random.normal()
        rates.append(rates[-1] + dr)
    return range(N+1), rates

if __name__ == "__main__":
    x, y = vasicek(0.007595, 0.1, 0.023353455187403, 0.00025142000827639, 0.5, 64)

    import matplotlib.pyplot as plt
    plt.plot(x,y)
    plt.show()
#%%
z= x,y
z
#%%