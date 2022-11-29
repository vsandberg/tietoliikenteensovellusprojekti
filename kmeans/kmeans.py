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
plt.show()







