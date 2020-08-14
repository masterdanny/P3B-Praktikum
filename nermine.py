import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import legendre

x = np.array([180, 172.933425610738, 165.893955739434, 158.909418821001, 152.009109282217, 145.224563330281, 138.590377890729, 132.145070558482, 125.93195832035, 120, 114.404497337886, 109.207479725344, 104.47751218593, 100.288585136763, 96.7177134641804, 93.8409657162581, 91.7279410723505, 90.4352300024699, 90, 0])
y = np.array([17.5, 17.2, 16.0, 14.6, 12.1, 9.4, 6.8, 2.9, 1.4, -2.9, -2.0, -5.2, -6.1, -8.0, -8.3, -8.4, -9.3, -9.8, -10.4, 1])
#np.polynomial.legendre.legfit(x, y, 2, rcond=None, full=False, w=None)
#x1 = np.linspace(180,0,400)
#y1 = np.array([(0.5*(3*(math.cos(x)**2)-1)) for x in [math.radians(r) for r in x1]])
#y1 = np.array([legendre(x) for x in x1])
plt.plot(x, y, 'bs',  color='black', markersize=2)
#plt.plot(x1, y1, 'r--', x, y, 'bs',  color='black', markersize=2)
plt.show()


