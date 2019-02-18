# Furijeova transformacija(redovi) i primena Batervortovog filtra niskih propusnih ucestanosti (lowpass)
# Davor Jordacevic 2016201251
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy import signal

# Kreiranje signala
t= np.arange( 0 , 2 , 0.001)
x= np.sin( 2*np.pi * 2 *t) + np.sin( 2*np.pi * 7 *t) + np.sin( 2*np.pi * 11 *t) + 0.25*np.random.randn(len(t))
# plt.plot(t,x)
# plt.show()

# Furijeova transformacija pocetnog signala
X=sp.fft(x)
Fs=1000     # Fs - perioda odabiranja 
f=np.linspace(0,Fs,len(x)+1)
f=f[:-1]
# plt.stem(f[0:50],np.abs(X[0:50]))
# plt.show()

# Kreiranje Batervortovog filtra i filtriranje signala
b, a = signal.butter(5,0.01 , btype ='low')         # (N,Wn ...) - (tip flitra , tacka od koje funkcija opada za -3dB
w, h = signal.freqz(b,a)
fNorm = w / sp.pi
f1 = fNorm * (Fs/2)
# plt.plot(f1, sp.absolute(h))
# plt.title('Filter')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
y = signal.lfilter(b,a,x)
# plt.plot(t,y)
# plt.show()

# Furijeova transformacija filtriranog signala
Y=sp.fft(y)
Fs=1000
f=np.linspace(0,Fs,len(y)+1)
f=f[:-1]
n=len(y)
plt.stem(f[0:50],np.abs(Y[0:50]))
plt.show()