# QAL_TV2a. Look how amplitude changes when varying the angles of the spherical resonator. Fit the Legendre Polynomial to the corresponding measured points.

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import numpy as np

def func(x,a,b):
	"""Defining Legendre Polynomial"""
	return a*0.5*(3*math.cos(x * math.pi/180)**2-1)+b

xdata = [180, 172.9334256, 165.8939557, 158.9094188, 152.0091093, 145.2245633, 138.5903779, 132.1450706, 125.9319583, 120, 114.4044973, 109.2074797, 104.4775122, 100.2885851, 96.71771346, 93.84096572, 91.72794107, 90.43523, 90]
ydata = [4.00000, 3.92000, 3.69000, 3.30000, 2.77000, 2.13000, 1.53000, 1.03000, 0.56000, 0.45000, 0.48000, 1.60000, 1.45000, 1.74000, 1.94000, 2.25000, 2.30000, 2.39000, 2.44000] 

#plt.plot(xdata, ydata)
#plt.show()

x, y = np.polynomial.legendre.Legendre.basis(3, [-1, 1]).linspace(100)
plt.plot(x, y, label=3)

plt.legend()
plt.plot()
plt.show()
