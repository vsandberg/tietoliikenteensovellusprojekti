import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA



def rows(data):
    numberOfRows = len(data)/3
    numberOfRows = int(numberOfRows)
    return numberOfRows

def randomData():
    random = np.random.randint(min,max,size=(4,3))
    return random

def dataprocessing(numberOfRows):
    datamatrix = np.zeros((numberOfRows,3))
    datamatrix[:,0] = data[0::3]
    datamatrix[:,1] = data[1::3]
    datamatrix[:,2] = data[2::3]
    return datamatrix

def kMeans(random,datamatrix):
    for k in range(10):
        centerPointCumulativeSum = np.zeros((4,3))
        Counts = np.zeros(4) 
        values = np.zeros(4)
        avgDistance = np.zeros((4,3))
        for i in range(numberOfRows):
            for j in range(4):
                value = np.abs(np.sqrt(np.power((random[j,0]- datamatrix[i,0]),2) + # X
                                np.power((random[j,1]- datamatrix[i,1]),2) +        # Y
                                np.power((random[j,2]- datamatrix[i,2]),2)))        # Z
                values[j] = value
            p = np.argmin(values)
            Counts[p] += 1
            centerPointCumulativeSum[p,0:3] += datamatrix[i,0:3]

            #Flag = np.min(Counts)
        for f in range(4):
            if Counts[f] == 0:
                avgDistance[f] = np.random.randint(min,max,size=3)

            else:
                avgDistance[f] = (centerPointCumulativeSum[f] / Counts[f])
                avgDistance = np.around(avgDistance,4) # kahden decimaalin tarkkuudella

        print(avgDistance, "\n")
        random = randomData()

        

    
        
            
            
            
        
        



    
if __name__=="__main__":
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
    global min
    global max
    global rounds
    rounds = 3
    min = np.min(data)
    max = np.max(data)
    random = randomData()
    numberOfRows = rows(data)
    datamatrix = dataprocessing(numberOfRows)
    kMeans(random,datamatrix)








