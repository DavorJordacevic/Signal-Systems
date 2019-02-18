import numpy as np
import matplotlib.pyplot as plt 
 
x= np.array([0,1,1,1,0])
h= np.array([0,1,1,0])

lx = len(x)
lh = len(h)

zerosh= np.zeros(lh)
x= np.concatenate((x,zerosh) , axis=0)

zerosx= np.zeros(lx)
h= np.concatenate((h,zerosx) , axis=0)

y=np.zeros(lx+lh-1)

# Racunanje konvolucije korak po korak
for n in range(1,lx+lh-1):
    y[n]=0
    for k in range (1,lx):
        if (n-k+1>0):
            y[n]= y[n] +x[k]*h[n-k+1]

plt.stem(y)
plt.show()