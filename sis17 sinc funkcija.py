import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-10,10,0.01)
x = np.sinc(t)

plt.plot(t,x)
plt.show()