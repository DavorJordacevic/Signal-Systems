import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,5,1)   # Funkcija koja pravi niz brojeva od -5(ukljucujuci) do 5(neukljucujuci) sa korakom 1
x=np.zeros(10)          # Funkcija koja pravi niz od 10 nula

x= np.exp(n)            # Eksponencijalna funkcija
#plt.stem(n,x)           # Stem se koristi za crtanje vremenski diskretnih signala
#plt.show()              # Show se koristi kako bi nam se slika prikazala u prozoru

xDelayed = np.roll(x,-2) # Funkcija roll se koristi za pomeranje signala ulevo i udesno 
plt.stem(n,xDelayed)
plt.show()