#Zadatak 2.4.2 Datoteka data.csv sadrži mjerenja visine i mase provedena na muškarcima i
#ženama. Skripta zadatak_2.py ucitava dane podatke u obliku numpy polja ˇ data pri cemu je u ˇ
#prvom stupcu polja oznaka spola (1 muško, 0 žensko), drugi stupac polja je visina u cm, a treci´
#stupac polja je masa u kg.
#a) Na temelju velicine numpy polja data, na koliko osoba su izvršena mjerenja? ˇ
#b) Prikažite odnos visine i mase osobe pomocu naredbe ´ matplotlib.pyplot.scatter.
#c) Ponovite prethodni zadatak, ali prikažite mjerenja za svaku pedesetu osobu na slici.
#d) Izracunajte i ispišite u terminal minimalnu, maksimalnu i srednju vrijednost visine u ovom ˇ
#podatkovnom skupu.
#e) Ponovite zadatak pod d), ali samo za muškarce, odnosno žene. Npr. kako biste izdvojili
#muškarce, stvorite polje koje zadrži bool vrijednosti i njega koristite kao indeks retka.
#ind = (data[:,0] == 1)

import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("data.csv", delimiter=",")
data = data[1:]

print("a) Number of people: ",len(data))

x=[data[:,1]]
y=[data[:,2]]
plt.figure(1)
plt.scatter(x,y,linewidth=0.1,marker='.')
plt.xlabel ("height ")
plt.ylabel (" weight ")
plt.title ( " b) ")
plt.show ()

x_50=[data[::50,1]]
y_50=[data[::50,2]]
plt.figure(2)
plt.scatter(x_50,y_50,linewidth=0.1,marker='.')        
plt.xlabel ("height ")
plt.ylabel (" weight ")
plt.title ( " c) ")
plt.show()

print("d) min height:",np.min(x),",max height:",np.max(x),",avg height:",np.mean(x))

m_x=[]
f_x=[]
for item in data:
  if(item[0]==1):
    m_x.append(item[1])
  else:
    f_x.append(item[1])

print("e)MALE: min height:",np.min(m_x),",max height:",np.max(m_x),",avg height:",np.mean(m_x),"\n FEMALE: min height:",np.min(f_x),",max height:",np.max(f_x),",avg height:",np.mean(f_x))