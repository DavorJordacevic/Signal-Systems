import numpy as np
import matplotlib.pyplot as plt

t = np.arange(1000,dtype=float)
t=t/1000      #  Hz

x=np.sin(2*np.pi*3*t)
plt.plot(t,x)
plt.show()

y=np.cos(2*np.pi*3*t)
plt.plot(t,y)
plt.show()