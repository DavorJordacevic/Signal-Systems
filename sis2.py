import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,5,1)   # Funkcija koja pravi niz brojeva od -5(ukljucujuci) do 5(neukljucujuci) sa
                        # korakom 1
x=np.zeros(10)          # Funkcija koja pravi niz od 10 nula
print(n)
print(x)

x= np.exp(n)            # Eksponencijalna funkcija
print(x)
plt.stem(n,x)           # Stem se koristi za crtanje vremenski diskretnih signala
plt.show()              # Show se koristi kako bi nam se slika prikazala u prozoru
  