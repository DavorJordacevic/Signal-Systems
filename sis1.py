 import numpy as np
 import matplotlib.pyplot as plt
 
 n= np.arange(-5,5,1)
 t= np.arange(-5,5,0.001)
 
 x=t**2
 y=n**2
 
 plt.plot(t,x)
 plt.show()
 
 plt.stem(n,y)
 plt.show()