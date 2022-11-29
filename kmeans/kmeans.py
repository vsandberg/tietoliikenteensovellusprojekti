import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.loadtxt('C:/Users/sandb/Desktop/koneoppimisenperusteet/projektiviikko5/putty.log')

datax = data[0::3]
datay = data[1::3]
dataz = data[2::3]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(datax,datay,dataz)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#plt.show()

numberOfRows = len(data)/3
numberOfRows = int(numberOfRows)
min = np.min(data)
max = np.max(data)

random = np.random.randint(min,max,size=(4,3))
print(random)

centerPointCumulativeSum = np.zeros((4,3)) # . Tähän summataan aina voittavalle keskipisteelle yhden datapisteen x,y,z komponentit.
print(centerPointCumulativeSum)

Counts = np.zeros((1,4)) # tänne kasvatetaan aina voittavan keskipisteen datapisteiden lukumäärää yhdellä jokaisen voiton jälkeen.
print(Counts)

Distances = np.zeros((1,4)) # tähän talletetaan laskennan edetessä yksittäisen x,y,z pisteen etäisyys kaikkiin keskipisteet datarakenteessa oleviin 4 keskipisteeseen ja nuo 4 etäisyysarvoa talletetaan tähän muuttujaan.
print(Distances)











