# Primer programa koji filtrira beli Gausov sum
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

Fs=1000
from scipy import signal
t=np.arange(0,2,0.001)
x= np.cos(2*np.pi*t*3)+0.5* np.cos(2*np.pi*t*11)
x1= x+np.random.randn(len(x))*0.5    #creates an array of specified shape and fills it with random values as per standard normal distribution.
#plt.plot(t,x1)

x1=sp.fft(x1)     #Return discrete Fourier transform of real or complex sequence.
print(len(x1))

f= np.arange(0,1,1./len(x1))
f=f*Fs
print(len(f))

#spektar signala kada je u signalu prisutani gausovski sum
#plt.plot(f[0:len(x1)/2] , abs(x1[0:len(x1)/2]))
b,a = signal.butter(4, 50.0/500)
#Design an Nth-order digital or analog Butterworth filter and return the filter coefficients.
w,h = signal.freqz(b,a,len(x1)/2)
#Compute the frequency response of a digital filter.
f1= w/sp.pi*Fs/2
#plt.plot(f1,abs(h))
plt.plot(1)
y=signal.lfilter(b,a,x1)
#Filter data along one-dimension with an IIR or FIR filter.
plt.subplot(211)
plt.plot(t,x1)
plt.subplot(212)
plt.plot(t,y,c='r')
plt.show()
#prvi signal je originalan, a drugi izfiltriran
#Sum ciji je frekvencijski deo smesten do 50 Hz nije uklonjen ovim procesom