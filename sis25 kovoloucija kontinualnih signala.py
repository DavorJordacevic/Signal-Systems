import numpy as np
import matplotlib.pyplot as plt
t = np.arange(-10,10,1)
u= 1.*(t>-1) - 1.*(t>0)

h= (1.*(t>0) - 1.*(t>2))+2*(1.*(t>2) - 1.*(t>3))

y= np.convolve(u,h)
plt.plot(y)
plt.show()