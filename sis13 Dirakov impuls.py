import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-10,10,1) # Funkcija koja pravi niz brojeva od -10(ukljucujuci) do 10(neukljucujuci) sa korakom 1
z=np.zeros(20)          # Funkcija koja pravi niz od 10 nula

z[-5]=1                 # Dirakov impuls u odredjenom trenutku ima vrednost 1


plt.stem(t,z)           # Stem se koristi za crtanje vremenski diskretnih signala
plt.show()              # Show se koristi kako bi nam se slika prikazala u prozoru