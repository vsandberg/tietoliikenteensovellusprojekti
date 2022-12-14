import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd


def rows(data):
    numberOfRows = len(data)
    numberOfRows = int(numberOfRows)
    return numberOfRows

def dataprocessing(numberOfRows,data):
    datamatrix = np.zeros((numberOfRows,3))
    datamatrix[:,0] = data.values[0::,5]
    datamatrix[:,1] = data.values[0::,6]
    datamatrix[:,2] = data.values[0::,7]
    position = data.values[0::,9]
    return datamatrix,position
    

def randomData(min,max):
    random = np.random.randint(min,max,size=(6,3))
    return random



def kMeans(random,datamatrix,position):
    for k in range(10):
        centerPointCumulativeSum = np.zeros((6,3))
        Counts = np.zeros(6) 
        values = np.zeros(6)
        flag = np.zeros(6)
        avgDistance = np.zeros((6,3))
        for i in range(numberOfRows):
            for j in range(6):
                value = np.abs(np.sqrt(np.power((random[j,0]- datamatrix[i,0]),2) + # X
                                np.power((random[j,1]- datamatrix[i,1]),2) +        # Y
                                np.power((random[j,2]- datamatrix[i,2]),2)))        # Z
                values[j] = value
            p = np.argmin(values)
            flag[p] = position[i]
            Counts[p] += 1
            centerPointCumulativeSum[p,0:3] += datamatrix[i,0:3]

        for f in range(6):
            if Counts[f] == 0:
                avgDistance[f] = np.random.randint(min,max,size=3)

            else:
                avgDistance[f] = (centerPointCumulativeSum[f] / Counts[f])
                avgDistance = np.around(avgDistance,4)


        random = avgDistance
        print(avgDistance, "\n")
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for i in range(numberOfRows):
        ax.scatter(datamatrix[:,0],datamatrix[:,1],datamatrix[:,2],color='g')
    for i in range(6):
        ax.scatter(avgDistance[:,0],avgDistance[:,1],avgDistance[:,2],marker='*',s=200,color='r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    
    
    headerData = avgDistance
    with open('projektiviikko5/keskipisteet.h', 'w') as f:
        line = "float w[6][6] = {"
        for i in range(5):
            line = line + "{"
            outputThis = np.array2string(headerData[i,:],precision=3,separator=',')
            line = line + outputThis[1:len(outputThis)-1]
            line = line + "," + str(int(flag[i]))
            line = line + "},"
        outputThis = np.array2string(headerData[5,:],precision=3,separator=',')
        line = line + "{"
        line = line + outputThis[1:len(outputThis)-1]
        line = line + "," + str(int(flag[5]))
        line = line + "}"
        line = line + "};"
        f.write(line)
        f.write('\n')
    f.close()

        


if __name__=="__main__":
    
    filename = "C:/Users/sandb/Desktop/koneoppimisenperusteet/projektiviikko5/file.csv"
    data = pd.read_csv(filename, delimiter=";")

    global min
    global max
    min = np.min(data.values[0::,5:7])
    max = np.max(data.values[0::,5:7])

    numberOfRows = rows(data)
    datamatrix,position = dataprocessing(numberOfRows,data)
    random = randomData(min,max)
    kMeans(random,datamatrix,position)







