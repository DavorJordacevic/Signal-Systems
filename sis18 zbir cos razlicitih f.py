import scipy as sp
import matplotlib.pyplot as plt

t = sp.arange(0,1,0.001)
x = 0.33 *sp.cos(2* sp.pi *10* t) - 0.1*sp.cos(2* sp.pi *3 * 10* t) + 0.05*sp.cos(2* sp.pi *5*10* t)

plt.plot(t,x)
plt.show()