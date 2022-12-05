import numpy as np 
from sklearn.metrics import confusion_matrix 
from numpy import genfromtxt  


rawData = genfromtxt('C:/Users/sandb/Desktop/koneoppimisenperusteet/projektiviikko5/putty_arduino.log', delimiter=',')  
y_true = rawData[:,0] 
y_pred = rawData[:,1] 
print(confusion_matrix(y_true, y_pred))