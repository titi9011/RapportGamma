import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


ydata = []

with open('Na 140degree detect1 et 2.txt') as f:
    for i in range(12):
        line = f.readline()
        if i == 11:
            nbdonne = int(line[2:])

    for i in range(nbdonne + 1):
        line = f.readline()
        ydata.append(float(line))



xdata = []
for i in range(len(ydata)):
    xdata.append(float(i))




plt.figure(figsize=(5,5))
plt.plot(xdata, ydata)
plt.xlabel('Fréquence')
plt.ylabel('Énergie')

plt.show()


