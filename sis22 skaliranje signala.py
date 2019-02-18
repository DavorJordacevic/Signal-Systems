import numpy as np
import matplotlib.pyplot as plt 
# Pocetni signal koji se crta je x[n] 
n= np.arange(-10,10,1)
n1=3*n    # Skaliranje x[3n]   Signal ce se pojavljivati na svake 3 sekunde 
n2=1/3*n  # Skaliranje x[1/3n]   Signal ce se pojavljivati na svaku 1/3 sekunde 
x=n 
y=n

plt.stem(n,x,'r')
plt.show()

plt.stem(n1,y,'g')
plt.show()

plt.stem(n2,y,'y')
plt.show()