import numpy as np
import matplotlib.pyplot as plt

#  Rad sa diskretnim signalim 
#  Diskretni signali su signali koji su definisani samo u odredjenim vremenskim trenucima 
#  Umesto vremenske ose t , koristi se n (odbirci)

n = np.arange(-10,10)

u0 = 1.*(n>=0) 
u3 = 1.*(n>=4)

u = u0 -  u3 

# plt.stem(n,u)
# plt.show()

# Konvolucija vremenski diskretnih signala 
# y[n] = x[n] * h[n]
x = u 

u_1 = 1.*(n>=-2) 
u2 = 1.*(n>=3)

u = u_1 -  u2 
h=u

# plt.stem(n,h)
# plt.show()

y = np.convolve(x,h)    # convolve - naredba za konvolucija dva signala

plt.stem(y)
plt.show()