import numpy as np
import matplotlib.pyplot as plt 

t = np.arange(-50,50)

x= np.cos(2* np.pi * t *0.05)

plt.stem(t,x)
plt.show()