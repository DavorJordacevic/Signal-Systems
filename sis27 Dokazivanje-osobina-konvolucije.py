import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10,10,1)

x1 = 1.*(n>=0)
x2 = 1.*(n>=2)
x3 = np.exp(-0.5*n)

# Dokazivanje komutacije
y=np.convolve(x1,x2)

y2=np.convolve(x2,x1)
# plt.subplot(2,1,1)
# plt.stem(y)
# plt.subplot(2,1,2)
# plt.stem(y2)
# plt.show()

# Dokazivanje distribucije u odnosu na sabiranje

y=x2+x3
y2=np.convolve(x1,y)
# plt.subplot(2,1,1)
# plt.stem(y2)

y=np.convolve(x1,x2)
y2=np.convolve(x1,x3)
y3=y+y2
# plt.subplot(2,1,2)
# plt.stem(y3)
# plt.show()

# Dokazivanje asocijacije

y=np.convolve(x1,x2)
y2=np.convolve(y,x3)
plt.subplot(2,1,1)
plt.stem(y2)

y=np.convolve(x2,x3)
y2=np.convolve(x1,y)
plt.subplot(2,1,2)
plt.stem(y2)
plt.show()

