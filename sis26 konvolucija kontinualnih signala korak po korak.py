import numpy as np
import matplotlib.pyplot as plt 
 
t = np.arange(-10,10,1)
x= 1.*(t>-1) - 1.*(t>0)

h= (1.*(t>0) - 1.*(t>2))+2*(1.*(t>2) - 1.*(t>3))

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

plt.plot(y)
plt.show()