import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Gauss(x, A, B, C):
    y = A * np.exp(-1/(2*B**2)*(x - C)**2)
    return y


ydata = []

with open('GPH-3004 Gamma_lab_1\Cs137 set 32 3min delay TSCA Gate.txt') as f:
    for i in range(12):
        line = f.readline()
        if i == 11:
            nbdonne = int(line[2:])
        
    for i in range(nbdonne + 1):
        line = f.readline()
        ydata.append(float(line))
        
    line = f.readline()
    line = f.readline()
    line = f.readline()
    
    
    debut_roi = int(line[:4])
    fin_roi = int(line[4:])



ydata = ydata[debut_roi:fin_roi]

xdata = []
for i in range(len(ydata)):
    xdata.append(float(i))



parameters, covariance = curve_fit(Gauss, xdata, ydata)
  
fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]


fit_y = Gauss(xdata, fit_A, fit_B, fit_C)



plt.figure(figsize=(10,10))
plt.plot(xdata, ydata)
plt.plot(xdata, fit_y, label='fit')
plt.xlabel('Fréquence')
plt.ylabel('Énergie')
plt.show()

LMH = 2*np.sqrt(2*np.log(2))*fit_B

print(LMH/32)


