import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-10,10,0.1)   # Funkcija koja pravi niz brojeva od -10(ukljucujuci) do 10(neukljucujuci) sa korakom 0.1
x=np.zeros(10)          # Funkcija koja pravi niz od 10 nula

u5= 1.*(t>=5)           # Hevisajdova funkcija ( uslov da je t vece ili jednako nula se moze menjati u zavisnosti od pocetnog trenutka skoka funcije            
u7= 1.*(t>=7)
 
w=u5 - u7               # Oduzimanje signala

plt.plot(t,w)           # Plot se koristi za crtanje vremenski kontinualnih signala
plt.show()              # Show se koristi kako bi nam se slika prikazala u prozoru