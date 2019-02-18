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

x = u 

h = np.exp(n)

# plt.stem(n,h)
# plt.show()

y = np.convolve(x,h)    # convolve - naredba za konvolucija dva signala

plt.stem(y)
plt.show()