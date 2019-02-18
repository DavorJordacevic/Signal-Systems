import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

from scipy import signal

# Formiranje vremenske ose i signala 
t= np.arange(0,2,0.001)
x = np.sin(2*np.pi*2*t) + np.sin (2*np.pi*7*t) + np.sin(2*np.pi*11*t) # + 0.25*np.random.randn(len(x)) # Sum
# plt.subplot(2,2,1)
# plt.plot(t,x)
# plt.show()

# Furieova transformacija signala

X=sp.fft(x)
Fs=1000
f=np.linspace(0,Fs,len(x)+1)
f=f[:-1]
n=len(x)
# plt.subplot(2,2,2)
# plt.stem(f[0:50],np.abs(X[0:50]))
# plt.show()

# Filtracija signala
# Batervortov filter

b, a = signal.butter(5,0.01 , btype ='low')
w, h = signal.freqz(b,a)
fNorm = w / sp.pi
f1 = fNorm * (Fs/2)
# plt.plot(f1, sp.absolute(h))
# plt.title('Filter')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.subplot(2,2,3)
y = signal.lfilter(b,a,x)
# plt.plot(t,y)

Y=sp.fft(y)
Fs=1000
f=np.linspace(0,Fs,len(y)+1)
f=f[:-1]
n=len(y)
# plt.subplot=(2,2,4)
plt.stem(f[0:50],np.abs(Y[0:50]))
plt.show()