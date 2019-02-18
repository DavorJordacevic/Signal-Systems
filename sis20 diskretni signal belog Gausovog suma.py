import numpy as np
import matplotlib.pyplot as plt 

noise = np.random.normal(0,1,100)   # Normalna gausova raspodela

plt.stem(noise)
plt.show()