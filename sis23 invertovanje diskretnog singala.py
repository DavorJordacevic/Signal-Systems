import numpy as np
import matplotlib.pyplot as plt 
 
n= np.arange(-5,5,1)

n_invert = n[::-1]  #invertovaneje niza n

plt.stem(n,np.exp(n_invert))
plt.show()