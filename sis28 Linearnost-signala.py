import numpy as np
import matplotlib.pyplot as plt

n= np.arange(-10,10,1)
x1=1.*(n>=0)
h1=np.exp(-0.5*x1)
x2 = 1.*(n>=2)
h2=np.exp(-0.5*x2)

#Konstante L i B
L= 2
B=1

#f(lx1[n]+Bx2[n])
f1=np.exp(-0.5*(L*x1+B*x2))

#ly1[n]+By2[n]
f2=L*np.exp(-0.5*x1)+B*np.exp(-0.5*x2)

plt.subplot(2,1,1)
plt.stem(f1)
plt.subplot(2,1,2)
plt.stem(f2)
plt.show()
# Signal nije linearan

