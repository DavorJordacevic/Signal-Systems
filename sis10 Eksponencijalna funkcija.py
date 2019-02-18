import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-10,10,0.1)   # Funkcija koja pravi niz brojeva od -10(ukljucujuci) do 10(neukljucujuci) sa korakom 0.1
x=np.zeros(10)          # Funkcija koja pravi niz od 10 nula          

x=np.exp(t)             # Eksponencijalna funkcija 

plt.plot(t,x)           # Plot se koristi za crtanje vremenski kontinualnih signala
plt.show()              # Show se koristi kako bi nam se slika prikazala u prozoru