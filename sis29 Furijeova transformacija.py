import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

from scipy import signal

# Formiranje vremenske ose i signala 
t= np.arange(0,2,0.001)
x = np.sin(2*np.pi*2*t) + np.sin (2*np.pi*7*t) + np.sin(2*np.pi*11*t) # + 0.25*np.random.randn(len(x)) # Sum
plt.subplot(2,1,1)
plt.plot(t,x)
plt.show()

# Furieova transformacija signala

X=sp.fft(x)
Fs=1000
f=np.linspace(0,Fs,len(x)+1)
f=f[:-1]
n=len(x)
plt.subplot(2,1,2)
plt.stem(f[0:50],np.abs(X[0:50]))
plt.show()
